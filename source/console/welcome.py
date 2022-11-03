# -*- coding: utf-8 -*-
"""Console script for modern-python-boilerplate."""
import click

from source import __version__


@click.command()
@click.version_option(version=__version__)
def main() -> int:
    """Console script for modern-python-boilerplate."""
    click.echo("Replace this message by putting your code into modern_python_boilerplate.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    main()  # pragma: no cover
