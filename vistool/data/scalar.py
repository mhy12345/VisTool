from .base_data import BaseData
from .utils import torch_to_numpy
class Scalar(BaseData):
    def __init__(self):
        super(Scalar, self).__init__()
        self.data = 0.0

    def update(self, data):
        data = torch_to_numpy(data)
        self.data = data

    def eval(self):
        return self.data
