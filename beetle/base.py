import yaml
import os


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


def default_copy(path, output):
    pass


class Includer(object):
    specific = {}

    def add(self, extensions, function):
        for extension in extensions:
            self.specific[extension] = function

    def __init__(self, folders):
        self.include = folders['include']
        self.output = folders['output']

    def __iter__(self):
        for folder, __, filenames in os.walk(self.include):
            for filename in filenames:
                origin = os.path.join(folder, filename)
                destination = origin.replace(self.include, self.output)
                with open(origin, mode='rb') as fo:
                    yield destination, fo.read()


class Writer(object):
    generators = []

    def add(self, generator):
        self.generators.append(generator)

    def write(self):
        for generator in self.generators:
            for destination, content in generator:
                destination_folder = os.path.dirname(destination)

                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)

                with open(destination, 'wb') as fo:
                    fo.write(content)
