from .builder import Builder
import yaml
import sys
import os


def main():
    if 'serve' in sys.argv:
        os.chdir('output')
        import SimpleHTTPServer
        import SocketServer

        PORT = 8000

        Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

        httpd = SocketServer.TCPServer(("", PORT), Handler)

        print("serving at port", PORT)
        httpd.serve_forever()

    else:
        with open('config.yaml') as f:
            config = yaml.load(f.read())
            builder = Builder(config)
            builder.run()
