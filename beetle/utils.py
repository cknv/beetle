import os


def make_destination(file_name, new_extension=None):
    __, destination = file_name.split(os.sep, 1)
    if new_extension:
        destination = change_extension(destination, new_extension)
    return destination


def change_extension(file_name, new_extension):
    base, __ = os.path.splitext(file_name)
    return '{base}.{extension}'.format(
        base=base,
        extension=new_extension,
    )
