import torch
from .data import find_data_using_name
from .window import find_window_using_name
import visdom


class VisTool:
    def __init__(self, env = 'main'):
        self.data = {}
        self.windows = {}
        self.env = env
        self.vis = visdom.Visdom(env = env)

    def register_data(self, name, type, *args, **kwargs):
        data = find_data_using_name(type)
        self.data[name] = data(*args, **kwargs)

    def register_window(self, name, type, *args, **kwargs):
        window = find_window_using_name(type)
        self.windows[name] = window(name = name, host = self,
                *args, **kwargs)

    def update(self, key, value):
        self.data[key].update(value)

    def __getitem__(self, key):
        return self.data[key].eval()

    def sync(self):
        for win in self.windows.values():
            win.sync()

