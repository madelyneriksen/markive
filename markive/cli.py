"""Main command line interface for Markive."""


import os
import subprocess
import shlex
import click

from markive import util


EDITOR = os.getenv('EDITOR', 'vim')
MARKIVE_DIR = os.path.expanduser(
    os.getenv('MARKIVE_DIR', os.path.expanduser("~/markive/"))
)


@click.group()
def main():
    """Markive is a personal journal and archiving tool.

    Create new journal entries using Markdown, save your progress, and visit them
    later.
    """


@main.command()
@click.option('--folder', type=click.Path(exists=False))
def write(folder):
    """Write in the current entry for the day.
    """
    folder = os.path.expanduser(folder) if folder else MARKIVE_DIR
    config = util.read_config(folder)
    file = util.get_current_entry(folder)
    os.makedirs(os.path.dirname(file), exist_ok=True)

    # Create the hook commands
    pre_hook = shlex.split(config['pre_write'])
    post_hook = shlex.split(config['post_write'])

    # Call all commands in sync
    if pre_hook:
        subprocess.call(pre_hook)
    subprocess.call([EDITOR, file])
    if post_hook:
        subprocess.call(post_hook)
