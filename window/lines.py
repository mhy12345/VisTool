import numpy as np
from .base_window import BaseWindow

class Lines(BaseWindow):
    def __init__(self, name, host, sources):
        super(Lines, self).__init__(name, host)
        self.sources = sources
        self.counter = 0

    def _send_data(self):
        t = []
        for src in self.sources:
            t.append(self.host[src])
        return np.array([t])

    def sync(self): 
        self.counter += 1
        self.host.vis.line(
                Y = self._send_data(),
                X = np.array([self.counter]),
                win = self.name, 
                update='append' if self.counter>1 else None,
                opts = {'legend':self.sources},
                )
