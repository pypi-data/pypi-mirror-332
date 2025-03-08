import logging
from pathlib import Path
from typing import Annotated, Optional

import typer
from rich.logging import RichHandler

from git_presets.cli.remove import remove_app
from git_presets.cli.set import set_app
from git_presets.cli.show import show_app
from git_presets.cli.unset import unset_app
from git_presets.cli.use import use_app
from git_presets.context import CliContextObject

app = typer.Typer(
    pretty_exceptions_show_locals=False,
    context_settings={"help_option_names": ["-h", "--help"]},
)


def verbose_callback(value: bool):
    if value:
        loglevel = logging.DEBUG
    else:
        loglevel = logging.INFO
    logging.basicConfig(handlers=[RichHandler()], format="%(message)s", level=loglevel)


def version_callback(value: bool):
    if value:
        print("0.1.0")
        raise typer.Exit()


@app.callback()
def callback(
    ctx: typer.Context,
    verbose: Annotated[
        bool,
        typer.Option(
            "--verbose", "-v", help="Enable verbose mode.", callback=verbose_callback
        ),
    ] = False,
    version: Annotated[
        bool,
        typer.Option(
            "--version",
            "-V",
            help="Print version and exit.",
            callback=version_callback,
            is_eager=True,
        ),
    ] = False,
    config_file: Annotated[
        Optional[Path],
        typer.Option(
            "--config-file",
            "-c",
            help="Path to the config file.",
            envvar="GIT_PRESETS_CONFIG_FILE",
        ),
    ] = None,
):
    ctx.obj = CliContextObject(config_file_path=config_file)


app.add_typer(use_app)
app.add_typer(set_app)
app.add_typer(unset_app)
app.add_typer(remove_app)
app.add_typer(show_app)
