"""Utility functions for Markive."""


import datetime
import os

import yaml


def get_current_entry(markive_folder: str) -> str:
    """Get the current entry based on today's date.

    Arguments:
        markive_folder: String path of where entries are stored

    Returns:
        entry: Today's entry as a filepath.
    """
    now = datetime.date.today()
    month = os.path.join(markive_folder, now.strftime("%B-%Y"))
    entry = os.path.join(month, now.strftime("%b-%d.md"))
    return entry


def read_config(markive_folder: str) -> dict:
    """Read the configuration YAML file from the Markive folder.

    Arguments:
        markive_folder: String path of the markive folder.

    Returns:
        config: Dictionary of configuration parameters.
    """
    config = {
        "pre_write": '',
        "post_write": '',
        "template": ("---\n"
                     "date: %Y-%m-%d\n"
                     "---\n"),
    }
    config_file = os.path.join(markive_folder, "config.yml")
    if os.path.exists(config_file):
        with open(config_file, 'r') as file:
            config.update(yaml.load(file.read()))
    return config
