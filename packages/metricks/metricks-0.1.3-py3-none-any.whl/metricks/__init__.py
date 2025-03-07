from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd
import yaml
from snowflake.snowpark.functions import col, function, lower
from snowflake.snowpark.table import Table

from metricks.metadata import METADATA_TABLE, get_definition
from metricks.metric import Filter, Metric, _Dimension
from metricks.pipelines import get_or_create_pipeline
from metricks.session import get_session


def load_metrics(path: Path) -> dict:
    raw_data = yaml.safe_load(path.read_text())
    return raw_data["metrics"]


def load_metric(path: Path, name: str) -> Metric:
    raw_data = yaml.safe_load(path.read_text())
    metric_data = raw_data["metrics"][name]
    metric_data["id"] = name
    return Metric.from_dict(metric_data)


def load_metric_from_dict(data: dict) -> Metric:
    return Metric.from_dict(data)


def validate_filters(
    dimensions: list[_Dimension] | None, filters: list[Filter] | None = None
) -> None:
    if filters is None:
        return

    dimension_columns = [] if dimensions is None else [dim.column for dim in dimensions]

    for filter in filters:
        if filter.column not in dimension_columns:
            raise ValueError(
                f"Filter column {filter.column} not in dimensions {dimension_columns}"
            )


def apply_filters(table: Table, filters: list[Filter] | None = None) -> Table:
    if filters is None:
        return table

    for filter in filters:
        if filter.equals is not None:
            table = table.filter(col(filter.column) == filter.equals)
        elif filter.between is not None:
            table = table.filter(
                col(filter.column).between(filter.between[0], filter.between[1])
            )
        elif filter.values is not None:
            table = table.filter(col(filter.column).isin(filter.values))
    return table


def apply_measures(
    metric: Metric,
    table: Table,
    measures: list[str] | None = None,
    group_by: list[str] | str | None = None,
) -> Table:
    if measures is None:
        return table

    agg_functions = []
    for _measure in measures:
        full_measure = metric.get_measure(_measure)
        # Pulls out the agg function and applies it to the column
        # e.g. sum(num_jobs) as num_jobs
        agg_functions.append(
            function(full_measure.agg)(col(full_measure.column)).alias(
                full_measure.column
            )
        )
    return table.group_by(group_by).agg(*agg_functions)


def get_metric_from_id(metric_id: str) -> Metric:
    definition = get_definition(metric_id)
    return load_metric_from_dict(definition)


def get_all_metrics(pattern: str | None = None) -> list[Metric]:
    """
    Get all metrics from the metadata table.

    If a pattern is provided, like `product.northstar.*`, it will return all
    metrics that match the pattern.
    """
    session = get_session()
    metadata_table = session.table(METADATA_TABLE)
    if pattern is not None:
        pattern = pattern.replace("*", "%")
        pattern = pattern.lower()
        metadata_table = metadata_table.filter(lower(col("metric_id")).like(pattern))

    metadata_table = metadata_table.select("metric_id").distinct()

    return [get_metric_from_id(row["METRIC_ID"]) for row in metadata_table.collect()]


def get_data_from_id(
    metric_id: str,
    measures: list[str] | None = None,
    group_by: list[str] | None = None,
    filters: list[Filter] | None = None,
) -> pd.DataFrame:
    """Get data from a pre-registered metric"""
    definition = get_definition(metric_id)
    metric = load_metric_from_dict(definition)
    return get_data(metric, measures, group_by, filters)


def _lowercase_columns(df: pd.DataFrame) -> pd.DataFrame:
    return df.rename(columns=lambda x: x.lower())


def get_data(
    metric: Metric,
    measures: list[str] | None = None,
    group_by: list[str] | None = None,
    filters: list[Filter] | None = None,
    lowercase_columns: bool = True,
) -> pd.DataFrame:
    """
    Get data from any metric. Note that this will also create the pipeline
    if it doesn't exist.
    """
    if metric.defaults is not None:
        defaults = deepcopy(metric.defaults)
        if measures is None:
            measures = defaults.get("measures", None)
        if group_by is None:
            group_by = defaults.get("group_by", None)
        if filters is None:
            _filters = defaults.get("filters", [])
            actual_filters = []
            for filter in _filters:
                if filter.get("last_days"):
                    last_days = filter.pop("last_days")
                    filter["between"] = (
                        datetime.now() - timedelta(days=last_days),
                        datetime.now(),
                    )
                actual_filters.append(Filter(**filter))
            filters = actual_filters

    if metric.prepared_table is not None:
        base_table = get_or_create_pipeline(metric)

        y_cols = metric.y if isinstance(metric.y, list) else [metric.y]
        cols = [metric.x, *y_cols]
        base_table = get_session().table(metric.prepared_table).select(cols)

        validate_filters(metric.dimensions, filters)
        base_table = apply_filters(base_table, filters)

        df = base_table.to_pandas()
        if lowercase_columns:
            df = _lowercase_columns(df)
        return df

    if metric.base_table is not None:
        base_table = get_or_create_pipeline(metric)

        validate_filters(metric.dimensions, filters)
        base_table = apply_filters(base_table, filters)

        base_table = apply_measures(metric, base_table, measures, group_by)

        df = base_table.to_pandas()
        if lowercase_columns:
            df = _lowercase_columns(df)
        return df

    if metric.query:
        df = get_session().sql(metric.query).to_pandas()
        if lowercase_columns:
            df = _lowercase_columns(df)
        return df

    raise ValueError("Either query or table must be provided")


def main() -> None:
    print("Welcome to metricks!")


if __name__ == "__main__":
    main()
