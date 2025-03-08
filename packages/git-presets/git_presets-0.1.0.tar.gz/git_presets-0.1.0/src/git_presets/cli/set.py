import logging
from typing import Annotated

import typer

from git_presets.attr import Attributes
from git_presets.config import Config
from git_presets.context import CliContextObject

logger = logging.getLogger(__name__)
set_app = typer.Typer()


@set_app.command()
def set(
    preset_name: Annotated[str, typer.Argument(help="Name of the preset.")],
    attribute: Annotated[Attributes, typer.Argument(help="Attribute to set.")],
    value: Annotated[str, typer.Argument(help="Value to set.")],
    ctx: typer.Context,
):
    """Set an attribute for a preset."""
    obj: CliContextObject = ctx.obj
    config = Config.from_config_file(obj.config_file_path)

    config.set_attribute(preset_name, attribute, value)

    config.write(obj.config_file_path)
    logger.info(f"Succesfully set {attribute} to {value} for preset {preset_name}")
