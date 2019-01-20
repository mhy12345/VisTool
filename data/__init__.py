import importlib
from .base_data import BaseData

def find_data_using_name(data_name):
    """Import the module "data/[data_name].py".
    In the file, the class called DatasetNameModel() will
    be instantiated. It has to be a subclass of BaseModel,
    and it is case-insensitive.
    """
    data_filename = ".data." + data_name 
    datalib = importlib.import_module(data_filename, package='vistool')
    data = None
    target_data_name = data_name.replace('_', '')
    for name, cls in datalib.__dict__.items():
        if name.lower() == target_data_name.lower() \
           and issubclass(cls, BaseData):
            data = cls

    if data is None:
        print("In %s.py, there should be a subclass of BaseModel with class name that matches %s in lowercase." % (data_filename, target_data_name))
        exit(0)

    return data

