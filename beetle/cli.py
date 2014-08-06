import importlib
from .builder import Builder
from .base import Config
import sys
import os


def render(config):
    builder = Builder(config)
    builder.run()


def main():
    config = Config.from_path('config.yaml')

    commands = {
        'render': render,
    }

    for plugin in config.plugins:
        a = importlib.import_module(plugin['name'])
        commands.update(a.commands)

    if len(sys.argv) > 1:
        command = sys.argv[1]

        commands[command](config)
