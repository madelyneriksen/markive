"""Test Markive utility functions."""


import datetime
from markive import util


def test_custom_date_entry():
    """Test the specific date entry creation function."""
    date = datetime.date(2017, 1, 31)
    target = util.get_current_entry('./', date=date)
    assert target.endswith('January-2017/Jan-31.md')


def test_hooks_falsy_by_default():
    """Test that the configuration returns falsy hooks by default.

    Sanity check."""
    config = util.read_config("some-nonexistant-path")
    assert not config["pre_write"]
    assert not config["post_write"]
