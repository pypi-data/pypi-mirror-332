from pathlib import Path


class ConfigFileNotFound(Exception):
    def __init__(self, path: Path):
        super().__init__(f"Config file is not found in {path}")


class PresetNotFound(Exception):
    def __init__(self, preset_name: str):
        super().__init__(f"Preset {preset_name} not found")
