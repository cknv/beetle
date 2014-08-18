import importlib
from .builder import Builder
from .base import Config
from .renderers import ContentRenderer
import sys


class Commander:
    commands = {}

    def add(self, command, function):
        self.commands[command] = function

    def run(self, command):
        self.commands[command]()

def main():
    config = Config.from_path('config.yaml')
    content_renderer = ContentRenderer.default()
    builder = Builder(config, content_renderer)
    commander = Commander()

    # Got to provide a command to render.
    commander.add('render', builder.run)

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
