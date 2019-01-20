from .base_data import BaseData
from .utils import torch_to_numpy

class Images(BaseData):
    def __init__(self):
        super(Images, self).__init__()
        self.data = None

    def update(self, data):
        data = torch_to_numpy(data)
        self.data = data

    def eval(self):
        return self.data
