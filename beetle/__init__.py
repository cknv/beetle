name = 'beetle'
version = '0.4.1-dev'
project_url = 'https://github.com/cknv/beetle'

class BeetleError(Exception):
    def __init__(self, message, page=None):
        # Crazy hackery to get a default message to the stacktrace.
        Exception.__init__(self, message)
        self.page = page
