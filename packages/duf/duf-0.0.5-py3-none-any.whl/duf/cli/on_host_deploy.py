from pathlib import Path

import click


@click.command
@click.option('-t', '--target')
def cli(target):
    print('target', target)


if __name__ == '__main__':
    cli()
