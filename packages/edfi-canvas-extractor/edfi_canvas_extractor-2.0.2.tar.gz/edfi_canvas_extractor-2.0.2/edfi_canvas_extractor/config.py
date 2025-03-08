# SPDX-License-Identifier: Apache-2.0
# Licensed to the Ed-Fi Alliance under one or more agreements.
# The Ed-Fi Alliance licenses this file to you under the Apache License, Version 2.0.
# See the LICENSE and NOTICES files in the project root for more information.

import logging
import os
import socket

from canvasapi.exceptions import CanvasException
from requests import RequestException
from sqlalchemy import create_engine
import sqlalchemy
from canvasapi import Canvas

logger = logging.getLogger(__name__)


def get_sync_db_engine(sync_database_directory: str) -> sqlalchemy.engine.base.Engine:
    """
    Create a SQL Alchemy Engine for a SQLite file

    Returns
    -------
    sqlalchemy.engine.base.Engine
        a SQL Alchemy Engine
    """
    logger.debug(
        "Ensuring database directory at %s", os.path.abspath(sync_database_directory)
    )
    os.makedirs(sync_database_directory, exist_ok=True)
    return create_engine(f"sqlite:///{sync_database_directory}/sync.sqlite")


def get_canvas_api(canvas_base_url: str, canvas_access_token: str) -> Canvas:
    """
    Create new CanvasAPI object for API communication

    Returns
    -------
    Canvas
        a new CanvasAPI object
    """
    return Canvas(canvas_base_url, canvas_access_token)


MAX_TOTAL_CALLS = 4
RETRY_WINDOW_AFTER_FIRST_CALL_IN_SECONDS = 600

RETRY_CONFIG = {
    "retry_on_exceptions": (
        IOError,
        CanvasException,
        RequestException,
        socket.timeout,
        socket.error,
        ConnectionError,
        ConnectionAbortedError,
    ),
    "max_calls_total": MAX_TOTAL_CALLS,
    "retry_window_after_first_call_in_seconds": RETRY_WINDOW_AFTER_FIRST_CALL_IN_SECONDS,
}
