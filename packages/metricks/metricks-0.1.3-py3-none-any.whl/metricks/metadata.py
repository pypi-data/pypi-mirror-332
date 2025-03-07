"""
Use a metadata table to track which metrics have been created, and saves
the metric definition in the metadata table.

metadata structure:
| metric_id (must be globally unique) | hash (sha256 of metric) | created_at |
"""

from __future__ import annotations

import json
import sys
from datetime import datetime

import pandas as pd
from loguru import logger
from snowflake.snowpark.functions import col
from snowflake.snowpark.table import Table

from metricks.metric import Metric
from metricks.session import get_session

logger.remove()
logger.add(sys.stderr, level="INFO")

METRICKS_SCHEMA = "temp.metricks"
METADATA_TABLE = f"{METRICKS_SCHEMA}.metadata"


def _create_metadata_table() -> Table:
    session = get_session()
    session.sql(
        f"create or replace table {METADATA_TABLE} (metric_id string, hash string, definition string, created_at timestamp)"
    ).collect()
    return session.table(METADATA_TABLE)


# Cache to avoid querying the metadata table for each metric
PIPELINE_CACHE: dict[str, str] = {}


def pipeline_exists(metric: Metric) -> bool:
    metric_id = metric.id
    metric_hash = metric.get_hash()

    if metric_id in PIPELINE_CACHE:
        return PIPELINE_CACHE[metric_id] == metric_hash

    session = get_session()
    metadata_table = session.table(METADATA_TABLE)
    try:
        metadata_table.limit(1).collect()
    except Exception:
        logger.error("Metadata table does not exist, creating it")
        metadata_table = _create_metadata_table()

    latest_created = (
        metadata_table.filter((col("metric_id") == metric_id))
        .sort(col("created_at").desc())
        .select(col("hash"))
        .limit(1)
        .collect()
    )

    if len(latest_created) > 0 and (latest_created[0]["HASH"] == metric_hash):
        PIPELINE_CACHE[metric_id] = metric_hash
        return True

    return False


def insert_metadata(metric: Metric) -> None:
    session = get_session()
    df = pd.DataFrame(
        {
            "metric_id": [metric.id],
            "hash": [metric.get_hash()],
            "definition": [json.dumps(metric.to_dict())],
            "created_at": [datetime.now()],
        }
    )
    sdf = session.create_dataframe(df)
    sdf.write.mode("append").save_as_table(METADATA_TABLE)


def get_definition(metric_id: str) -> dict:
    session = get_session()
    metadata_table = session.table(METADATA_TABLE)
    definition_str = (
        metadata_table.filter(col("metric_id") == metric_id)
        .sort(col("created_at").desc())
        .select(col("definition"))
        .limit(1)
        .collect()[0]["DEFINITION"]
    )
    return json.loads(definition_str)
