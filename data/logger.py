from .base_data import BaseData
class Logger(BaseData):
    def __init__(self, max_size = 99):
        super(Logger, self).__init__()
        self.data = ''
        self.max_size = max_size

    def update(self, data):
        self.data += data + '<br/>'

    def eval(self):
        return self.data

    def clear(self):
        self.data = ''
