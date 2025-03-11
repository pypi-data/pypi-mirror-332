import os
from pathlib import Path

import loguru
from environs import env
from rich.console import Console

from liblaf import grapes

from . import DEFAULT_FILTER, Filter


def console_handler(
    console: Console | None = None,
    filter_: Filter | None = None,
) -> "loguru.HandlerConfig":
    if console is None:
        console = grapes.logging_console()
    if filter_ is None:
        filter_ = DEFAULT_FILTER

    def sink(message: "loguru.Message") -> None:
        console.print(message, end="", no_wrap=True, crop=False, overflow="ignore")

    return {
        "sink": sink,
        "format": "[green]{time:YYYY-MM-DD HH:mm:ss.SSS}[/green] | [logging.level.{level}]{level: <8}[/logging.level.{level}] | [cyan]{name}[/cyan]:[cyan]{function}[/cyan]:[cyan]{line}[/cyan] - {message}",
        "filter": filter_,
    }


def file_handler(
    fpath: str | os.PathLike[str] | None = None, filter_: Filter | None = None
) -> "loguru.HandlerConfig":
    if fpath is None:
        fpath = env.path("LOGGING_FILE", default=Path("run.log"))
    return {"sink": fpath, "filter": filter_, "mode": "w"}


def jsonl_handler(
    fpath: str | os.PathLike[str] | None = None, filter_: Filter | None = None
) -> "loguru.HandlerConfig":
    if fpath is None:
        fpath = env.path("LOGGING_JSONL", default=Path("run.log.jsonl"))
    return {"sink": fpath, "filter": filter_, "serialize": True, "mode": "w"}
