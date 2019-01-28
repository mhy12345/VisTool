import torch
from .data import find_data_using_name
from .window import find_window_using_name
import visdom
import logging
logger = logging.getLogger(__name__)


class VisTool:
    def __init__(self, env = 'main'):
        self.data = {}
        self.windows = {}
        self.env = env
        self.vis = visdom.Visdom(env = env)
        self.counter = 0
        logger.info("visdom instance created <%s>..."%env)

    def register_data(self, name, type, *args, **kwargs):
        data = find_data_using_name(type)
        self.data[name] = data(*args, **kwargs)
        self.data[name]._type = type
        self.print_info()

    def register_window(self, name, type, *args, **kwargs):
        window = find_window_using_name(type)
        self.windows[name] = window(name = name, host = self,
                *args, **kwargs)
        self.windows[name]._type = type
        self.print_info()

    def print_info(self):
        text = ''
        text += '<h1>Variables</h1>'
        text += '<table border="1"><tr><th>Name</th><th>Type</th></tr>'
        for w in self.data:
            text += '<tr><td>%s</td><td>%s</td>'%(w, self.data[w]._type)
        text += '</table>'
        text += '<h1>Windows</h1>'
        text += '<table border="1"><tr><th>Name</th><th>Type</th></tr>'
        for w in self.windows:
            text += '<tr><td>%s</td><td>%s</td>'%(w, self.windows[w]._type)
        text += '</table>'
        self.vis.text(text, win='_log')

    def update(self, key, value):
        if isinstance(value, torch.Tensor):
            value = value.detach()
        self.data[key].update(value)

    def __getitem__(self, key):
        return self.data[key].eval()

    def sync(self, disp_freq=1):
        self.counter += 1
        if self.counter >= disp_freq:
            self.counter = 1
        else:
            return 
        for key,win in self.windows.items():
            try:
                win.sync()
            except Exception as e:
                logger.warn('Cannot sync window %s'%key)
                logger.warn('%s'%e)

