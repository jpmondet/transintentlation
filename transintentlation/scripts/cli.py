# Skeleton of a CLI

import click

import transintentlation

import diffios


@click.command('transintentlation')
@click.argument('count', type=int, metavar='N')
def cli(count):
    """Echo a value `N` number of times"""
    for i in range(count):
        click.echo(transintentlation.has_legs)
