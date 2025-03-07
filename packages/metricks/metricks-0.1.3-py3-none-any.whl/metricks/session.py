from __future__ import annotations

import os
import sys
from pathlib import Path

from loguru import logger
from snowflake.snowpark import Session
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.exceptions import SnowparkSessionException, SnowparkSQLException
from tomlkit import parse

# Show 'info' by default
logger.remove()
logger.add(sys.stderr, level="INFO")

docs_log = (
    "https://docs.snowflake.com/en/developer-guide/snowflake-cli/"
    "connecting/configure-connections#define-connections"
)

_active_session: Session | None = None


def get_session() -> Session:
    """Uses the Snowflake config file to create a session."""
    global _active_session

    if _active_session is not None:
        return _active_session

    try:
        _active_session = get_active_session()
        return _active_session
    except (SnowparkSessionException, SnowparkSQLException):
        pass

    config_file = Path.home() / ".snowflake" / "config.toml"

    if not config_file.exists():
        raise ValueError(
            "Snowflake config file not found. "
            "Please create a file at ~/.snowflake/config.toml. "
            f"See {docs_log} for more information."
        )

    config = parse(config_file.read_text())

    connection_name = os.environ.get("SNOWFLAKE_DEFAULT_CONNECTION_NAME", "default")

    try:
        settings: dict = config["connections"][connection_name]
    except (KeyError, TypeError) as e:
        raise ValueError(
            f"Connection name {connection_name} not found in config file. "
            "Please set the SNOWFLAKE_DEFAULT_CONNECTION_NAME environment variable."
        ) from e

    _active_session = Session.builder.configs(settings).create()
    return _active_session
