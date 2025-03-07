"""
Creates helpful SQL functions for querying metrics

NOT YET WORKING, STILL THINKING THROUGH THE API
"""

from __future__ import annotations

from snowflake.snowpark.functions import sproc
from snowflake.snowpark.session import Session

from metricks.session import get_session


def get_metric_table(metric_id: str) -> str:
    schema = "temp.metricks"
    return f"{schema}.{metric_id.replace('.', '__')}"


def query_metric_table(session: Session, metric_id: str) -> str:  # noqa: ARG001
    return get_metric_table(metric_id)


def create_or_replace_sproc_for_test():
    sproc(
        query_metric_table,
        name="temp.metricks.query_metric",
        stage_location="@temp.metricks.sprocs",
        replace=True,
        is_permanent=True,
        session=get_session(),
        packages=[],
    )


if __name__ == "__main__":
    ...
    # create_or_replace_sproc_for_test()
    # session = get_session()
    # print(query_metric_table(session, "product.northstar.ns_credits_breakdown"))
