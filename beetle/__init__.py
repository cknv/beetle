name = 'beetle'
version = '0.4.1-dev'
project_url = 'https://github.com/cknv/beetle'

class BeetleError(Exception):
    def __init__(self, page=None):
        self.page = page
