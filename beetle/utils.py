import os


def read_folder(folder, mode):
    for folder, __, files in os.walk(folder):
        for file_name in files:
            path = os.path.join(folder, file_name)
            with open(path, mode) as fo:
                yield path, fo.read()
