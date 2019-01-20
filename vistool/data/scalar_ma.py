from .base_data import BaseData
from .utils import torch_to_numpy

class ScalarMA(BaseData):
    def __init__(self, max_size = 160):
        super(ScalarMA, self).__init__()
        self.max_size = max_size
        self.data = []

    def update(self, data):
        data = torch_to_numpy(data)
        if len(self.data) == self.max_size:
            self.data = self.data[1:]
        self.data.append(data)

    def eval(self):
        if len(self.data) == 0:
            return 0.0
        else:
            return sum(self.data)/len(self.data)
