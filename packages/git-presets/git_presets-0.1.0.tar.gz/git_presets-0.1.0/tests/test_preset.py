from git_presets.attr import Attributes
from git_presets.config import Preset


def test_set_attribute(work_preset: Preset):
    work_preset.set_attribute(Attributes.USER_NAME, "foobar")
    assert work_preset.user_name == "foobar"


def test_unset_attribute(work_preset: Preset):
    work_preset.set_attribute(Attributes.USER_NAME, None)
    assert work_preset.user_name is None
