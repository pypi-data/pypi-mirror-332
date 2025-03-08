from logging import getLogger
from typing import Annotated

import typer

from git_presets.attr import Attributes
from git_presets.config import Config
from git_presets.context import CliContextObject

logger = getLogger(__name__)
unset_app = typer.Typer()


@unset_app.command()
def unset(
    preset_name: Annotated[str, typer.Argument(help="Name of the preset.")],
    attribute: Annotated[Attributes, typer.Argument(help="Attribute to unset.")],
    ctx: typer.Context,
):
    """Unset an attribute for a preset."""
    obj: CliContextObject = ctx.obj
    config = Config.from_config_file(obj.config_file_path)

    config.unset_attribute(preset_name, attribute)

    config.write(obj.config_file_path)
    logger.info(f"Succesfully unset {attribute} for preset {preset_name}")
