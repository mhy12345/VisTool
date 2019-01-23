from .base_window import BaseWindow

class Bar(BaseWindow):
    def __init__(self, name, host, source):
        super(Bar, self).__init__(name, host)
        self.source = source

    def sync(self): 
        self.host.vis.bar(self.host[self.source], win = self.name)
