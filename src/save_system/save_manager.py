"""
class to handle saving and loading game files.
save file will be stored in user_data_dir.
"""

import json
from pathlib import Path
from typing import Any, Dict, Type

from platformdirs import user_data_dir

# interfaces
from .save_interfaces.world import World

# app config
APP_NAME = "didactic-disco"
APP_AUTHOR = "gs-games"

# data config
DATA_DIR = Path(user_data_dir(APP_NAME, APP_AUTHOR))
DATA_DIR.mkdir(parents=True, exist_ok=True)
SAVE_FILE = DATA_DIR / "didactic-disco-save-file.json"

class SaveManager:
    _save_data: Dict[str, Any] = {}
    _section_classes: Dict[str, Type] = {
        "world": World,
    }

    @classmethod
    def load_save_game(cls):
        """
        Load saved data from disk into memory.
        """
        if SAVE_FILE.exists():
            with open(SAVE_FILE, "r") as f:
                raw = json.load(f)
        else:
            raw = {}

        for name, section_class in cls._section_classes.items():
            section_data = raw.get(name)
            if section_data is not None:
                cls._save_data[name] = section_class(**section_data)
            else:
                cls._save_data[name] = section_class()

    @classmethod
    def get(cls, section: str):
        """
        Retrieve an in-memory section by name.
        """
        return cls._save_data[section]

    @classmethod
    def push(cls):
        """
        Save all section data to disk (overwrite entire save file).
        """
        to_save = {}
        for name, obj in cls._save_data.items():
            to_save[name] = obj.__dict__  # dataclasses convert cleanly
        with open(SAVE_FILE, "w") as f:
            json.dump(to_save, f, indent=2)

    @classmethod
    def reset(cls):
        """
        Clears the in-memory save data. Useful for testing or starting over.
        """
        cls._save_data.clear()
