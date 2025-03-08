import logging
import os.path
from pathlib import Path
from typing import Optional

from pydantic import BaseModel
from rich.console import Console
from rich.table import Table

from git_presets.attr import Attributes
from git_presets.exceptions import PresetNotFound

appname = "git-presets"
default_config_path = Path(os.path.expanduser("~/.config/git-presets/config.json"))
logger = logging.getLogger(__name__)


class Preset(BaseModel):
    preset_name: str
    user_name: Optional[str] = None
    user_email: Optional[str] = None

    def set_attribute(self, attribute: Attributes, value: Optional[str]) -> None:
        if attribute == Attributes.USER_NAME:
            self.user_name = value
        elif attribute == Attributes.USER_EMAIL:
            self.user_email = value
        else:
            raise ValueError(f"Unknown attribute: {attribute}")

    def print_in_table(self, console: Console):
        table = Table("Attribute", "Value")
        table.add_row(
            Attributes.USER_NAME,
            self.user_name if self.user_name is not None else "<not set>",
        )
        table.add_row(
            Attributes.USER_EMAIL,
            self.user_email if self.user_email is not None else "<not set>",
        )
        console.print(table)


class Config(BaseModel):
    presets: Optional[list[Preset]] = None

    @classmethod
    def from_config_file(cls, path: Optional[Path] = None) -> "Config":
        if path is None:
            path = default_config_path
        if not path.exists():
            return cls()
        json_string = path.read_text()
        config = cls.model_validate_json(json_string)
        return config

    def write(self, path: Optional[Path] = None) -> None:
        if path is None:
            path = default_config_path
        path.parent.mkdir(parents=True, exist_ok=True)
        json_string = self.model_dump_json()
        path.write_text(json_string)

    def remove_preset(self, preset_name: str) -> None:
        if self.presets is None:
            raise PresetNotFound(preset_name)

        n_presets = len(self.presets)
        self.presets = [p for p in self.presets if p.preset_name != preset_name]
        if n_presets == len(self.presets):
            raise PresetNotFound(preset_name)

    def get_preset(self, preset_name: str) -> Preset:
        if self.presets is None:
            raise PresetNotFound(preset_name)

        preset = next((p for p in self.presets if p.preset_name == preset_name), None)
        if preset is None:
            raise PresetNotFound(preset_name)
        return preset

    def set_attribute(
        self, preset_name: str, attribute: Attributes, value: Optional[str]
    ) -> None:
        if self.presets is None:
            self.presets = []

        preset_idx = next(
            (i for i, p in enumerate(self.presets) if p.preset_name == preset_name),
            None,
        )

        if preset_idx is None:
            logger.info(f"Preset {preset_name} not found. Creating new preset.")
            preset = Preset(preset_name=preset_name)
            preset.set_attribute(attribute, value)
            self.presets.append(preset)
        else:
            preset = self.presets[preset_idx]
            preset.set_attribute(attribute, value)

    def unset_attribute(self, preset_name: str, attribute: Attributes) -> None:
        preset = self.get_preset(preset_name)

        preset.set_attribute(attribute, None)
