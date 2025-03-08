from pathlib import Path

import pytest

from git_presets.attr import Attributes
from git_presets.config import Config
from git_presets.exceptions import PresetNotFound


def test_add_preset(empty_config: Config):
    empty_config.set_attribute("work", Attributes.USER_NAME, "jane doe")
    preset = empty_config.get_preset("work")
    assert preset.preset_name == "work"
    assert preset.user_name == "jane doe"


def test_update_preset(config_with_presets: Config):
    config_with_presets.set_attribute("work", Attributes.USER_NAME, "foobar")
    preset = config_with_presets.get_preset("work")
    assert preset.user_name == "foobar"


def test_unset(config_with_presets: Config):
    config_with_presets.unset_attribute("work", Attributes.USER_NAME)
    preset = config_with_presets.get_preset("work")
    assert preset.user_name is None


def test_remove_preset(config_with_presets: Config):
    config_with_presets.remove_preset("work")
    with pytest.raises(PresetNotFound):
        config_with_presets.get_preset("work")


def test_write_load(tmp_path: Path, config_with_presets: Config):
    config_path = tmp_path / "config.json"
    config_with_presets.write(config_path)
    loaded_config = Config.from_config_file(config_path)
    assert loaded_config == config_with_presets
