"""Utility functions for Markive."""


import datetime
import os


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
