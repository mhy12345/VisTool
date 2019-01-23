from .base_data import BaseData
from .utils import torch_to_numpy
import numpy as np

class Images(BaseData):
    def __init__(self):
        super(Images, self).__init__()
        self.data = None

    def update(self, data):
        data = torch_to_numpy(data)
        if len(data.shape) == 2:
            data = np.expand_dims(data, 0)
        if len(data.shape) == 3:
            data = np.expand_dims(data, 1)
        self.data = data

    def eval(self):
        return self.data
