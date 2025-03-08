import logging
from typing import Annotated

import typer

from git_presets.config import Config
from git_presets.context import CliContextObject

logger = logging.getLogger(__name__)


remove_app = typer.Typer()


@remove_app.command()
def remove(
    preset_name: Annotated[str, typer.Argument(help="Name of the preset to remove.")],
    ctx: typer.Context,
):
    """Remove a preset."""
    obj: CliContextObject = ctx.obj
    config = Config.from_config_file(obj.config_file_path)
    config.remove_preset(preset_name)
    config.write(obj.config_file_path)
    logger.info(f"Successfully removed preset {preset_name}")
