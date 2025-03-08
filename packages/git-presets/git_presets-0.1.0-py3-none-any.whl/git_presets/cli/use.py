import logging
import subprocess
from typing import Annotated

import typer

from git_presets.config import Config
from git_presets.context import CliContextObject

use_app = typer.Typer()
logger = logging.getLogger(__name__)


@use_app.command()
def use(
    preset_name: Annotated[str, typer.Argument(help="Name of the preset to use.")],
    ctx: typer.Context,
):
    """Update git config using the selected preset."""
    obj: CliContextObject = ctx.obj
    config = Config.from_config_file(obj.config_file_path)
    preset = config.get_preset(preset_name)

    if preset.user_name is not None:
        logger.debug(f"Setting user.name to {preset.user_name}")
        subprocess.run(["git", "config", "user.name", preset.user_name])
        logger.info(f"Successfully set user.name to {preset.user_name}")
    else:
        logger.debug("Unsetting user.name")
        subprocess.run(["git", "config", "--unset", "user.name"])
        logger.info("Successfully unset user.name")

    if preset.user_email is not None:
        logger.debug(f"Setting user.email to {preset.user_email}")
        subprocess.run(["git", "config", "user.email", preset.user_email])
        logger.info(f"Successfully set user.email to {preset.user_email}")
    else:
        logger.debug("Unsetting user.email")
        subprocess.run(["git", "config", "--unset", "user.email"])
        logger.info("Successfully unset user.email")
