from .base_data import BaseData
from .utils import torch_to_numpy
import  numpy as np

class ImageGallery(BaseData):
    def __init__(self, max_size = 80):
        super(ImageGallery, self).__init__()
        self.max_size = max_size
        self.data = None

    def update(self, data):
        data = torch_to_numpy(data)
        if len(data.shape) == 2:
            data = np.expand_dims(data, 0)
        if len(data.shape) == 3:
            data = np.expand_dims(data, 1)
        if self.data is None:
            self.data = data
        elif self.data.shape[0] < self.max_size:
            self.data = np.concatenate((data, self.data), 0)
        else:
            self.data = np.concatenate( ( data, np.split(self.data,[self.max_size-1,1],0)[0]), 0)

    def eval(self):
        return self.data
