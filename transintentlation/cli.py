""" Ugly command line that will should be prettier over time.
For now it does the job.

Usage :
    transintentlation intent.cfg n9k.cfg --help
"""

import click
from jinja2 import Environment, FileSystemLoader
import ruamel.yaml as yaml  # pylint: disable=useless-import-alias

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
@click.option('--variables',
              type=click.Path(exists=True, dir_okay=False),
              default=None,
              help='In case you provide a .j2 file as the "intent_config", you \
can pass a variables YAML file with this option')
# pylint: disable=too-many-arguments
def cli(intent_config,
        running_config,
        missing,
        additional,
        apply_missing,
        delete_additional,
        diff,
        variables):
    """ Show the cmds to apply to conform with the intent config by default"""

    if variables:
        intent_config = _render_template(intent_config, variables)
    print('='*100)
    print('!COMMANDS TO BE IN SYNC WITH THE INTENT CONFIG:')
    print('='*100)
    translate = Translate(intent_config, running_config)
    translate.apply_all_configs()
    print('='*100)

    if missing:
        miss = Comparing(intent_config, running_config)
        print('='*100)
        print('MISSING CONFIG')
        print(miss.pprint_missing())
        print('='*100)
    if additional:
        add = Comparing(intent_config, running_config)
        print('='*100)
        print('ADDITIONAL CONFIG:')
        print(add.pprint_additional())
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
        delta = Comparing(intent_config, running_config)
        print('='*100)
        print('SHOWING THE DIFF BETWEEN THE 2 CONFIGS')
        print(delta.delta())


def _render_template(template, variables):
    """ With a template .j2 and variables as .yaml,
    renders the final config """

    with open(variables, 'r') as vars_file:
        varsf = yaml.safe_load(vars_file)

    env = Environment(loader=FileSystemLoader(''))
    template = env.get_template(template)
    config = template.render(varsf)
    with open('/tmp/rendered_config', 'w') as rendered:
        rendered.write(config)
    return '/tmp/rendered_config'
