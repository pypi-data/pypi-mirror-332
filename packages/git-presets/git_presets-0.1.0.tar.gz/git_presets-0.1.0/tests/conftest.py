from unittest.mock import MagicMock

import pytest
from pytest_mock import MockerFixture

from git_presets.config import Config, Preset


@pytest.fixture
def work_preset() -> Preset:
    return Preset(
        preset_name="work",
        user_name="John Doe",
        user_email="johndoe@examplecompany.tld",
    )


@pytest.fixture
def private_preset() -> Preset:
    return Preset(
        preset_name="private", user_name="john", user_email="john@example.tld"
    )


@pytest.fixture
def empty_config() -> Config:
    return Config()


@pytest.fixture
def config_with_presets(work_preset: Preset, private_preset: Preset) -> Config:
    config = Config()
    config.presets = [work_preset, private_preset]
    return config


@pytest.fixture(autouse=True, scope="function")
def mock_subprocess_run(mocker: MockerFixture) -> MagicMock:
    return mocker.patch("subprocess.run")
