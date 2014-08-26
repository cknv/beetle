import yaml


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

    def __init__(self, folders, output):
        self.folders = folders
        self.output = output

    def __call__(self):
        for path in folders:
            pass
        if extension in self.specific:
            self.specific[extension]()
        else:
            default_copy(path, output)
