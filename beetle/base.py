import yaml
import os

from .utils import read_folder, remove_leading_folder


class Config:
    def __init__(self, data):
        self.folders = {
            'content': 'content',
            'output': 'output',
            'templates': 'templates',
            'include': 'include',
        }
        self.page_defaults = {}
        self.site = {}
        self.plugins = []

        if data is not None:
            # Aha! We have a config, lets update accordingly.
            self.folders.update(data.get('folders', {}))
            self.site.update(data.get('site', {}))
            self.page_defaults.update(data.get('page_defaults', {}))
            self.plugins = data.get('plugins', [])

    @classmethod
    def from_path(cls, path):
        with open(path) as fo:
            data = yaml.load(fo.read())
            return cls(data)


class Includer(object):
    def add(self, extensions, function):
        for extension in extensions:
            self.specific[extension] = function

    def read(self, path, content):
        partial_path, extension = os.path.splitext(path)
        extension = extension.strip('.')

        suggested_path = remove_leading_folder(path)
        if extension in self.specific:
            handler = self.specific[extension]
            suggested_path, content = handler(content, suggested_path)

        return suggested_path, content

    def __init__(self, folders):
        self.include = folders['include']
        self.output = folders['output']
        self.specific = {}

    def __iter__(self):
        for path, content in read_folder(self.include, 'rb'):
            yield self.read(path, content)


class Writer(object):
    def __init__(self, output_folder):
        self.output_folder = output_folder
        self.generators = []

    def add(cls, generator):
        cls.generators.append(generator)

    def files(self):
        for generator in self.generators:
            for destination, content in generator:
                yield destination, content

    def write(self):
        for destination, content in self.files():
            self.write_file(destination, content)

    def write_file(self, destination, content):
        full_destination = os.path.join(self.output_folder, destination)

        destination_folder = os.path.dirname(full_destination)
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        with open(full_destination, 'wb') as fo:
            fo.write(content)
