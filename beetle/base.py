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
