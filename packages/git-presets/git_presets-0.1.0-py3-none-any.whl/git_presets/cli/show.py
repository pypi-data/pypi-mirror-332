import logging
from typing import Optional

import typer
from rich import print
from rich.console import Console
from typing_extensions import Annotated

from git_presets.config import Config
from git_presets.context import CliContextObject
from git_presets.exceptions import PresetNotFound

logger = logging.getLogger(__name__)

console = Console()
show_app = typer.Typer()


@show_app.command()
def show(
    ctx: typer.Context,
    preset_name: Annotated[
        Optional[str],
        typer.Argument(
            help="Name of the preset to show. If not provided, all presets will be shown."
        ),
    ] = None,
):
    """Show the values of a preset."""
    obj: CliContextObject = ctx.obj
    config = Config.from_config_file(obj.config_file_path)
    if config.presets is None:
        logger.info("No presets found")
        return

    if preset_name is None:
        # show all
        for preset in config.presets:
            print(preset.preset_name)
            preset.print_in_table(console)
        return

    preset = next((p for p in config.presets if p.preset_name == preset_name), None)
    if preset is None:
        raise PresetNotFound(preset_name)
    preset.print_in_table(console)
