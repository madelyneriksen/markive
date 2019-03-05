"""Test Markive utility functions."""


import datetime
from markive import util


def test_current_entry():
    """Test the current entry creation function."""
    target_file = datetime.date.today().strftime("%b-%d.md")
    actual_target = util.get_current_entry('./')
    assert actual_target.endswith(target_file)


def test_hooks_falsy_by_default():
    """Test that the configuration returns falsy hooks by default.

    Sanity check."""
    config = util.read_config("some-nonexistant-path")
    assert not config["pre_write"]
    assert not config["post_write"]
