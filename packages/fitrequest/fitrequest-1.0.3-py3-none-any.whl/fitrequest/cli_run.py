import asyncio
import inspect
import sys
from collections.abc import Callable
from typing import Any

import makefun
import rich
import typer
from httpx import HTTPError

from fitrequest.errors import FitRequestConfigurationError, FitRequestRuntimeError


def run_pretty(func: Callable) -> Callable:
    """
    Simplify running fitrequest methods from the CLI, supporting both synchronous and asynchronous functions.
    The results are pretty-printed using 'rich' for enhanced readability.
    """

    def wrapper(*args, **kwargs) -> None:
        try:
            results = asyncio.run(func(*args, **kwargs)) if inspect.iscoroutinefunction(func) else func(*args, **kwargs)
        except (FitRequestConfigurationError, FitRequestRuntimeError, HTTPError) as err:
            rich.print(err)
            sys.exit(1)

        rich.print(results)

    # Remove **kwargs argument if it exists
    try:
        signed_wrapper = makefun.wraps(func, remove_args=['kwargs'])(wrapper)
    except KeyError:
        signed_wrapper = makefun.wraps(func)(wrapper)
    return signed_wrapper


@classmethod
def cli_app(cls: Any) -> typer.Typer:
    """
    Set up a CLI interface using Typer.
    Instantiates the fitrequest client, registers all its methods as commands, and returns the typer the application.
    """
    app = typer.Typer()
    client = cls()

    for attr_name in dir(client):
        attr = getattr(client, attr_name)

        if callable(attr) and (getattr(attr, 'fit_method', False) or getattr(attr, 'cli_method', False)):
            app.command()(run_pretty(attr))
    return app


@classmethod
def cli_run(cls: Any) -> None:
    """
    Runs the typer application.
    """
    cls.cli_app()()
