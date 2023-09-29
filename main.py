# -*- coding: utf-8 -*-
"""
This file is distributed as part of the StudentRepoBackups Project.
The source code may be available at
https://github.com/MrKelpy/StudentRepoBackups

If a license applies for this project, the former can be found
in every distribution, as a "LICENSE" file at top level.
"""

# Built-in Imports
import os
import time

# Third Party Imports
os.environ["GIT_PYTHON_GIT_EXECUTABLE"] = r"C:\Program Files\Git\bin\git.exe"
from git import Repo

# Local Application Imports
from utils.Config import Config


# noinspection PyBroadException
def create_backup(configuration: Config) -> None:
    """
    Creates a backup of the repositories present in the config file
    :param configuration: The configuration object
    :return: Void
    """

    backups_path: str = configuration.get_config("backups_path")
    configuration_dictionary: dict = configuration.get_groups()
    print(f"Preparing to clone the repositories into {backups_path}")

    # Iterate over the groups and clone the repositories into the backup folder
    for group_name in configuration_dictionary:

        try:
            url: str = configuration_dictionary[group_name]
            url = url.replace("https://", f"https://{configuration.get_config('github-login')}@")

            # Create the date formatting for the clone-in folder
            date = time.strftime("%d.%m.%Y.%H.%M.")

            # Clone the repository into the folder with the name of the group
            destination = os.path.join(backups_path, group_name, date)

            # Create the destination folder if it doesn't exist
            os.makedirs(destination, exist_ok=True)

            # Clone the repo
            Repo.clone_from(url, destination)
            print(f"Cloned {group_name} into {backups_path}")

        except:
            print(f"Failed to clone {group_name} (Is the configuration correct?)")
            continue


if __name__ == "__main__":
    """
    Main entrypoint of the program. Runs the normal program flow calling
    the defined functions in functional programming style.
    """

    config: Config = Config("./data/config.toml")
    delay: int = int(config.get_config("delay"))

    while True:
        create_backup(config)
        time.sleep(delay)
