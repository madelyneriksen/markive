Markive - Personal Archiving and Journaling Tool
======

Markive is a tool created for writing journal entries or records by date, using the command line and your text editor.

## Install :snake:

You will need an installation of Python 3.5+ to get started. Currently, the only way to install Markive is from source:

```bash
git clone https://github.com/madelyneriksen/markive/ .
virtualenv .env && source .env/bin/activate
python setup.py install
```

## Get Started :rocket:

Markive reads your environment variables to determine where it should write files, as well as what editor it should use by default. You can change the defaults by adding the following to your `.bashrc`, `.zshrc`, or any other profile:

```bash
# Where Markive stores files
export MARKIVE_DIR="/path/to/your/folder/"
# What editor Markive uses
export EDITOR="vim"
```

Now you are all set to create your first entry! Try it:

```bash
markive write
```

## Hacking Markive :computer:

Markive is simple in concept and execution, but is designed to be extensible and customizable. Changing the behavior of Markive is done with a YAML file at `$MARKIVE_DIR/config.yml`

**Hooks**

Create custom pre- and post-write hooks with Markive in the config file, by declaring them under `pre_write` and `post_write`.

```yaml
pre_write: |
  echo "I'm a shell command!"

post_write: |
  echo "I'm also a shell command!"
```

That's right, Markive let's you easily create a **cloud agnostic, fully automated** backup system, [without using FTP](https://news.ycombinator.com/item?id=9224). Auto sync with git is trivial:

```yaml
post_write: |
  git add -a && git commit -m "Markive auto-commit" && git push
```

**Templates**

Start all your files off with a default template! The standard Markive template looks something like this:

```yaml
---
date: <today's date>
---
```

This can easily be swapped in your config file:

```yaml
template: |
  ---
  date: %Y-%m-%d
  author: Maddie
  ---
```

Now, all **new** entries will have your custom template inserted at the top.

Variables for dates are inserted using Python's `datetime.strftime()` method. To see all available variables, visit the [documentation](https://docs.python.org/3/library/datetime.html?highlight=datetime#strftime-and-strptime-behavior).

### FAQ

* Why does this need to exist?

    My `~/Documents` folder is filled with multiple journal folders, all with different formats. It's confusing and difficult to search, so I needed a new tool.

    Also, I wanted to automatically insert pandoc information so I can convert my journal to a private website.

* Why the name Markive?

    I originally wanted to name the project "Marchive", but I decided to squeeze in a Markdown pun, at the expense of losing the month and plant puns.

* Why Python and not awk+sed+date+cat?

    Markive is simple and would be easy to make as a bash script. In fact, I encourage you to if you'd like! I did choose to write in Python3 for a few reasons though.

    I love Click CLI interfaces, and unlike tons of bash commands it's easier for me to remember how to make a new entry (`markive write`). If the goal is fostering good habits, **make it easy** to do the right thing. Plus, in the future I can extend markive easily.

### License

Markive is licensed under the terms of the MIT License. For full terms, please see the [LICENSE](/LICENSE) file.
