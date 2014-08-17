import importlib
from .builder import Builder
from .base import Config
from .renderers import ContentRenderer
import sys
import os

class Commander:
    commands = {}

    def __init__(self):
        self.add('help', self.help, 'Show this help output')

    def add(self, command, function, help='(No description available)'):
        self.commands[command] = {
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
    commander = Commander()

    # Got to provide a command to render.
    commander.add('render', builder.run, 'Render the site')

    for plugin_config in config.plugins:
        plugin_module = importlib.import_module(plugin_config['name'])
        plugin_module.register(
            plugin_config,
            config,
            commander,
            builder,
            content_renderer
        )

    if len(sys.argv) > 1:
        command = sys.argv[1]
        commander.run(command)
    else:
        commander.help()
