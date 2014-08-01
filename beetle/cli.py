from .builder import Builder
from .base import Config
import sys
import os

commands = {}

def register_subcommand(command, function):
    commands[command] = function

def serve(config):
    output_folder = config.folders['output']
    os.chdir(output_folder)
    import SimpleHTTPServer
    import SocketServer

    PORT = 8000

    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

    httpd = SocketServer.TCPServer(("", PORT), Handler)

    print("serving at port", PORT)
    httpd.serve_forever()

register_subcommand('serve', serve)

def main():
    config = Config.from_path('config.yaml')

    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command in commands:
            commands[command](config)
        else:
            print('unknown command...?')

    else:
        builder = Builder(config)
        builder.run()
