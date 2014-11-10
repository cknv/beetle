name = 'Beetle'
version = '0.7.1'
project_url = 'https://github.com/cknv/beetle'

class BeetleError(Exception):
    def __init__(self, message, page=None):
        self.message = message
        self.page = page

    def __str__(self):
        return self.message
