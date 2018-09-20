""" Ugly command line that will should be prettier over time.
For now it does the job.

Usage :
    transintentlation intent.cfg n9k.cfg --help
"""

import click

from transintentlation import Comparing, Translate


@click.command('transintentlation', help='Show the commands to apply to be in \
sync with the intent config by default. \
Options can be used by passing --OPTION_NAME=True')
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
@click.option('--diff',
              type=bool,
              default=False,
              help='Show only the diff between the 2 configs')
# pylint: disable=too-many-arguments
def cli(intent_config,
        running_config,
        missing,
        additional,
        apply_missing,
        delete_additional,
        diff):
    """ Show the cmds to apply to conform with the intent config by default"""

    print('='*100)
    print('COMMANDS TO BE IN SYNC WITH THE INTENT CONFIG:')
    translate = Translate(intent_config, running_config)
    translate.apply_all_configs()
    print('='*100)

    if missing:
        diff = Comparing(intent_config, running_config)
        print('='*100)
        print('MISSING CONFIG')
        print(diff.pprint_missing())
        print('='*100)
    if additional:
        diff = Comparing(intent_config, running_config)
        print('='*100)
        print('ADDITIONAL CONFIG:')
        print(diff.pprint_additional())
        print('='*100)
    if apply_missing:
        print('='*100)
        print('COMMANDS TO APPLY THE MISSING CONFIG:')
        translate.to_apply()
        print('='*100)
    if delete_additional:
        print('='*100)
        print('COMMANDS TO DELETE THE ADDITIONAL CONFIG:')
        translate.to_delete()
        print('='*100)
    if diff:
        diff = Comparing(intent_config, running_config)
        print('='*100)
        print('SHOWING THE DIFF BETWEEN THE 2 CONFIGS')
        print(diff.delta())
