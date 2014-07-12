from .builder import Builder
import yaml


def main():
    with open('config.yaml') as f:
        config = yaml.load(f.read())
        builder = Builder(config)
        builder.run()
