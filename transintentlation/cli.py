""" Ugly command line to do some tests """

import click

from transintentlation import Comparing


@click.command('transintentlation', help='Show the diff between the configs')
@click.argument('intent_config', type=click.Path(exists=True, dir_okay=False))
@click.argument('running_config', type=click.Path(exists=True, dir_okay=False))
@click.option('--missing',
              type=bool,
              default=False,
              help='Show only the missing config')
@click.option('--additional',
              type=bool,
              default=False,
              help='Show only the additional config')
@click.option('--apply_missing',
              type=bool,
              default=False,
              help='Show the commands to apply the missing config')
@click.option('--delete_additional',
              type=bool,
              default=False,
              help='Show the commands to delete the additional config')
def cli(intent_config,
        running_config,
        missing,
        additional,
        apply_missing,
        delete_additional):
    """ Show the diff by default"""

    diff = Comparing(intent_config, running_config)
    if missing:
        print('='*100)
        print('MISS')
        print(diff.pprint_missing())
        print('='*100)
    elif additional:
        print('='*100)
        print('ADD:')
        print(diff.pprint_additional())
        print('='*100)
    elif apply_missing:
        print('Not implemented yet')
    elif delete_additional:
        print('Not implemented yet')
    else:
        print('='*100)
        print('DELTA:')
        print(diff.delta())

