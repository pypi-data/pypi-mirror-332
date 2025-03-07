"""
Create a pipeline for a metric.

If a metric already exists, we should just use the existing pipeline, which
by default can be found at `temp.metricks.${metric_id}`.

If not, we should create a new pipeline and add it to the metadata table.

If the metric already exists, but the hash has changed, we should update the
metadata table and create a new pipeline.

The created pipeline should be a full-refresh dynamic table.

How do we determine the minimal set of dimensions and measures to create a pipeline?

Should a single metric have a single pipeline, or should we have a pipeline per
measure, or per combination of dimensions and measures?
"""

from __future__ import annotations

import sys

from loguru import logger
from snowflake.snowpark.functions import (
    col,
    current_date,
    date_add,
    date_trunc,
    function,
)
from snowflake.snowpark.table import Table

from metricks.metadata import METRICKS_SCHEMA, insert_metadata, pipeline_exists
from metricks.metric import Metric
from metricks.session import get_session

logger.remove()
logger.add(sys.stderr, level="INFO")


def get_pipeline_table_name(metric_id: str) -> str:
    table_name = metric_id.replace(".", "__")
    return f"{METRICKS_SCHEMA}.{table_name}"


def get_or_create_pipeline(metric: Metric) -> Table:
    session = get_session()
    table_name = get_pipeline_table_name(metric.id)

    if pipeline_exists(metric):
        return session.table(table_name)

    logger.info(f"Pipeline {metric.id} does not exist, creating it")
    _create_pipeline(metric)

    return session.table(table_name)


def get_sql_for_metric(metric: Metric) -> str:
    session = get_session()
    if metric.base_table is not None:
        object_type = "view"
    elif metric.prepared_table is not None:
        object_type = "table"
    elif metric.query is not None:
        return metric.query
    else:
        raise ValueError("Metric has no base_table or prepared_table or query")

    object_name = get_pipeline_table_name(metric.id)

    resp = session.sql(
        f"select get_ddl('{object_type}', '{object_name}') as definition"
    ).collect()

    print(resp)

    return resp[0]["DEFINITION"]


def _create_dynamic_table_pipeline(metric: Metric) -> None:
    session = get_session()
    table_name = get_pipeline_table_name(metric.id)

    group_by_columns = []
    if metric.dimensions is not None:
        for dim in metric.dimensions:
            if dim.original_column is not None:
                if dim.transform is not None:
                    if dim.type == "date":
                        new_column = date_trunc(
                            part=dim.transform,
                            expr=col(dim.original_column),
                        ).alias(dim.column)
                    else:
                        raise NotImplementedError(
                            f"Transform {dim.transform} not supported for type {dim.type}"
                        )
                else:
                    new_column = col(dim.original_column).alias(dim.column)

                group_by_columns.append(new_column)
            else:
                group_by_columns.append(col(dim.column))

    if metric.measures is None:
        aggregate_columns = []
    else:
        aggregate_columns = [
            function(measure.agg)(col(measure.column)).alias(measure.column)
            for measure in metric.measures
        ]

    resulting_table = (
        session.table(metric.base_table)
        .group_by(group_by_columns)
        .agg(*aggregate_columns)
    )

    # Filter by date_col
    if metric.date_col is not None and metric.days_back is not None:
        resulting_table = resulting_table.filter(
            col(metric.date_col)
            >= date_add(
                col=current_date(),
                num_of_days=-metric.days_back,
            )
        )

    resulting_table.create_or_replace_dynamic_table(
        table_name,
        lag="12 hours",
        warehouse=session.get_current_warehouse(),
    )


def _create_view_pipeline(metric: Metric) -> None:
    session = get_session()
    view_name = get_pipeline_table_name(metric.id)

    session.table(metric.prepared_table).create_or_replace_view(view_name)


def _create_pipeline(metric: Metric) -> None:
    if pipeline_exists(metric):
        logger.info(f"Pipeline {metric.id} already exists")
        return

    """
    product.northstar.jobs.overview": {
        "title": "Jobs Overview",
        "description": "Shows number of daily jobs and xp_jobs",
        "x": "ds",
        "y": ["num_jobs", "num_xp_jobs"],
        "base_table": "snowscience.northstar.ns_jobs_breakdown_aggregated",
        "defaults": {
            "group_by": ["ds"],
            "measures": ["num_jobs", "num_xp_jobs"],
        },
        "dimensions": [
            {
                "column": "snowflake_account_type",
                "type": "string",
                "values": ["Customer", "Partner", "Internal"],
            },
            {
                "column": "ds",
                "type": "date",
            },
        ],
        "measures": [
            {
                "column": "num_jobs",
                "type": "number",
                "agg": "sum",
            },
            {
                "column": "num_xp_jobs",
                "type": "number",
                "agg": "sum",
            },
        ],
        "chart_type": "line",
        "date_col": "ds",
        "y_label": "Number of Jobs",
    },
    """

    """
    select
        ds,
        snowflake_account_type,
        sum(num_jobs) as num_jobs,
        sum(num_xp_jobs) as num_xp_jobs
    from snowscience.northstar.ns_jobs_breakdown_aggregated
    group by ds, snowflake_account_type
    """

    if metric.base_table is not None:
        _create_dynamic_table_pipeline(metric)
    elif metric.prepared_table is not None:
        _create_view_pipeline(metric)
    else:
        raise NotImplementedError("Pipeline type not supported")

    table_name = get_pipeline_table_name(metric.id)

    logger.info(f"Created pipeline {table_name} for metric {metric.id}")

    insert_metadata(metric)

    logger.info(f"Inserted metadata for metric {metric.id}")
