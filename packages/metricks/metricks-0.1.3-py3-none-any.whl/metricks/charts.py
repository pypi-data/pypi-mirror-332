from __future__ import annotations

import pandas as pd
import streamlit as st

from metricks import get_data, get_metric_from_id
from metricks.metric import Filter, Metric
from metricks.pipelines import get_sql_for_metric


def line_chart(data: pd.DataFrame, x: str, y: list[str] | str):
    st.line_chart(data, x=x, y=y)


def bar_chart(data: pd.DataFrame, x: str, y: list[str] | str):
    st.bar_chart(data, x=x, y=y)


def area_chart(data: pd.DataFrame, x: str, y: list[str] | str):
    st.area_chart(data, x=x, y=y)


def get_chart(metric: Metric, data: pd.DataFrame):
    chart_type = metric.chart_type
    if chart_type == "line":
        return line_chart(data, metric.x, metric.y)

    if chart_type == "stacked_bar":
        return bar_chart(data, metric.x, metric.y)

    if chart_type == "area":
        return area_chart(data, metric.x, metric.y)

    raise ValueError(f"Unknown chart type: {chart_type}")


def get_chart_for_metric(
    metric: Metric,
    measures: list[str] | None = None,
    group_by: list[str] | None = None,
    filters: list[Filter] | None = None,
):
    data = get_data(metric, measures=measures, group_by=group_by, filters=filters)
    return get_chart(metric, data)


def get_chart_by_metric_id(
    metric_id: str,
    measures: list[str] | None = None,
    group_by: list[str] | None = None,
    filters: list[Filter] | None = None,
):
    metric = get_metric_from_id(metric_id)
    return get_chart_for_metric(
        metric,
        measures=measures,
        group_by=group_by,
        filters=filters,
    )


def show_tile(
    metric: Metric,
    *,
    measures: list[str] | None = None,
    group_by: list[str] | None = None,
    filters: list[Filter] | None = None,
):
    chart, data_preview, sql, description = st.tabs(
        ["Chart", "Data preview", "SQL", "Description"]
    )
    data = get_data(metric, measures=measures, group_by=group_by, filters=filters)
    sql_definition = get_sql_for_metric(metric)

    with chart:
        get_chart(metric, data)
    with data_preview:
        st.dataframe(data)
    with sql:
        st.code(sql_definition, language="SQL")
    with description:
        st.write(metric.description)
