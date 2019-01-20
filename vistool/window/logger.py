from .base_window import BaseWindow

class Logger(BaseWindow):
    def __init__(self, name, host, source):
        super(Logger, self).__init__(name, host)
        self.source = source

    def sync(self): 
        self.host.vis.text(self.host[self.source], win = self.name, append=True)
