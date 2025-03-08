from pathlib import Path
from unittest.mock import MagicMock

import pytest
from typer.testing import CliRunner

from git_presets.config import Config
from git_presets.exceptions import PresetNotFound
from git_presets.main import app

runner = CliRunner()


def test_use(
    tmp_path: Path, config_with_presets: Config, mock_subprocess_run: MagicMock
):
    config_path = tmp_path / "config.json"
    config_with_presets.write(config_path)
    result = runner.invoke(app, ["--config-file", str(config_path), "use", "work"])
    assert result.exit_code == 0
    mock_subprocess_run.assert_any_call(["git", "config", "user.name", "John Doe"])
    mock_subprocess_run.assert_any_call(
        [
            "git",
            "config",
            "user.email",
            "johndoe@examplecompany.tld",
        ]
    )


def test_set(tmp_path: Path, empty_config: Config) -> None:
    config_path = tmp_path / "config.json"
    empty_config.write(config_path)
    result = runner.invoke(
        app,
        ["--config-file", str(config_path), "set", "work", "user.name", "foobar"],
    )
    assert result.exit_code == 0
    assert config_path.exists()
    loaded_config = Config.from_config_file(config_path)
    assert loaded_config.presets is not None
    assert loaded_config.get_preset("work").user_name == "foobar"


def test_unset(tmp_path: Path, config_with_presets: Config) -> None:
    config_path = tmp_path / "config.json"
    config_with_presets.write(config_path)
    result = runner.invoke(
        app,
        [
            "--config-file",
            str(config_path),
            "unset",
            "work",
            "user.name",
        ],
    )
    assert result.exit_code == 0

    loaded_config = Config.from_config_file(config_path)
    assert loaded_config.get_preset("work").user_name is None


def test_remove(tmp_path: Path, config_with_presets: Config) -> None:
    config_path = tmp_path / "config.json"
    config_with_presets.write(config_path)
    result = runner.invoke(app, ["--config-file", str(config_path), "remove", "work"])
    assert result.exit_code == 0

    loaded_config = Config.from_config_file(config_path)
    with pytest.raises(PresetNotFound):
        loaded_config.get_preset("work")


def test_show_work_preset(tmp_path: Path, config_with_presets: Config) -> None:
    config_path = tmp_path / "config.json"
    config_with_presets.write(config_path)
    result = runner.invoke(app, ["--config-file", str(config_path), "show", "work"])
    assert result.exit_code == 0
    assert "John Doe" in result.stdout
    assert "johndoe@examplecompany.tld" in result.stdout


def test_show_all_presets(tmp_path: Path, config_with_presets: Config) -> None:
    config_path = tmp_path / "config.json"
    config_with_presets.write(config_path)
    result = runner.invoke(app, ["--config-file", str(config_path), "show"])
    assert result.exit_code == 0
    assert "John Doe" in result.stdout
    assert "john" in result.stdout
    assert "john@example.tld" in result.stdout
    assert "johndoe@examplecompany.tld" in result.stdout
