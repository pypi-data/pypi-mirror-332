from pathlib import Path
from typing import Optional


class CliContextObject:
    def __init__(self, config_file_path: Optional[Path] = None):
        self.config_file_path = config_file_path
