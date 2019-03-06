"""Main command line interface for Markive."""


import os
import datetime
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

    Create new journal entries using Markdown, save your progress, and edit
    them later. Markive is fully extensible, with pre- and post-write hooks
    defined in a config file.
    """


@main.command()
@click.option('--folder',
              type=click.Path(exists=False),
              help="Markive folder, if not $MARKIVE_DIR")
@click.option('--date',
              type=str,
              help="Date to create an entry for, in YYYY-MM-DD format (default now)")
def write(folder, date):
    """Write in the current entry for the day.

    Creates a folder named `<Month>-<Year>` in $MARKIVE_DIR, if it does
    not exist. Entry filenames are saved by date with names of `<Mo>-<Day>.md`
    by default.

    Configuration is stored in $MARKIVE_DIR/config.yml by default.
    """
    folder = os.path.expanduser(folder) if folder else MARKIVE_DIR
    if date:
        date = datetime.datetime.strptime(date, "%Y-%m-%d")
    else:
        date = datetime.datetime.now()

    config = util.read_config(folder)
    file = util.get_current_entry(folder, date)
    os.makedirs(os.path.dirname(file), exist_ok=True)

    # CD into the directory with this process
    os.chdir(folder)

    # Create the hook commands
    pre_hook = config['pre_write']
    post_hook = config['post_write']

    # Pre write commands
    if pre_hook:
        click.secho("Calling pre-write hook commands...", fg="blue")
        subprocess.call(pre_hook, shell=True)

    # Writing a formatted template to the file first if it's empty.
    if not os.path.exists(file):
        with open(file, 'w') as entry:
            entry.write(
                date.strftime(config['template'])
            )
    subprocess.call([EDITOR, file])

    # Post write commands
    if post_hook:
        click.secho("Calling post-write hook commands...", fg="blue")
        subprocess.call(post_hook, shell=True)
