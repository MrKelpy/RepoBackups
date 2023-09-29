# -*- coding: utf-8 -*-
"""
This file is distributed as part of the StudentRepoBackups Project.
The source code may be available at
https://github.com/MrKelpy/StudentRepoBackups

If a license applies for this project, the former can be found
in every distribution, as a "LICENSE" file at top level.
"""

# Built-in Imports
import os.path
from pathlib import Path

# Third Party Imports
import toml

# Local Application Imports


class Config:
    """
    This class defines a custom configuration reader for the program.
    """

    def __init__(self, path: str):
        self.path: Path = Path(path)
        self.__create_config()
        self.config: dict = self.__read_config()

    def get_config(self, key: str) -> str:
        """
        Returns a value from the config file based on the key.
        :param key: The key to look for in the dictionary
        :return: str or None
        """

        return self.config.get(key, "")

    def get_groups(self) -> dict:
        """
        Returns a dictionary containing all the groups defined in the configuration
        file for ease of use
        :return:
        """

        return self.config.get("groups", dict())

    def __read_config(self) -> dict:
        """
        Reads the configuration file present in the path and returns
        a dictionary based on the contents.
        :return: dict<str, str> with the configuration
        """

        with open(self.path, "r") as f:
            config = toml.load(f)

        return config

    def __create_config(self) -> None:
        """
        Writes the configuration to the file present in the path if it doesn't exist.
        :return: Void
        """

        # If the file already exists, don't do anything
        if os.path.exists(self.path):
            return

        os.makedirs(self.path.parent, exist_ok=True)

        # Otherwise, create the file with the default configuration
        config_dict: dict = {"groups": {"Grupo 1": "https://example.com", "Grupo 2": "https://example.com"},
                             "delay": 60*60*2, "backups_path": "./data/backups/",
                             "github-login": "token"}

        # ... and write it to the file
        with open(self.path, "w") as f:
            toml.dump(config_dict, f)
