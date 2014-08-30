import importlib
from .builder import Builder
from .base import Config, Includer, Writer
from .renderers import ContentRenderer
import shutil
import sys
import os


def cleaner(folders):
    def clean():
        shutil.rmtree(folders['output'])
        os.mkdir(folders['output'])
    return clean


class Commander:
    commands = {}

    def __init__(self):
        self.add('help', self.help, 'Show this help output')

    @classmethod
    def add(cls, command, function, help='(No description available)'):
        cls.commands[command] = {
            'function': function,
            'help': help
        }

    def run(self, command):
        self.commands[command]['function']()

    def help(self):
        print('Available commands:')
        commands_list = sorted(self.commands.keys())
        longest_command = len(max(commands_list, key=len))

        for command in commands_list:
            print('    - {0}:{1} {2}'.format(
                command,
                ' ' * (longest_command - len(command)),
                self.commands[command]['help']
            ))


def main():
    config = Config.from_path('config.yaml')
    content_renderer = ContentRenderer.default()
    builder = Builder(config, content_renderer)
    includer = Includer(config.folders)

    writer = Writer()
    writer.add(includer)
    writer.add(builder)

    commander = Commander()

    # Got to provide a command to render.
    commander.add('render', writer.write, 'Render the site')
    commander.add('clean', cleaner(config.folders), 'Delete rendered output')

    for plugin_config in config.plugins:
        plugin_module = importlib.import_module(plugin_config['name'])
        plugin_module.register(plugin_config, config)

    if len(sys.argv) > 1:
        bin_beetle, *args = sys.argv
        for command in args:
            commander.run(command)
    else:
        commander.help()
