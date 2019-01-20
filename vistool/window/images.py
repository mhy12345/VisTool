from .base_window import BaseWindow

class Images(BaseWindow):
    def __init__(self, name, host, source):
        super(Images, self).__init__(name, host)
        self.source = source

    def sync(self): 
        self.host.vis.images(self.host[self.source], win = self.name)
