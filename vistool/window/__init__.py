import importlib
from .base_window import BaseWindow

def find_window_using_name(window_name):
    """Import the module "window/[window_name].py".
    In the file, the class called DatasetNameModel() will
    be instantiated. It has to be a subclass of BaseModel,
    and it is case-insensitive.
    """
    window_filename = ".window." + window_name 
    windowlib = importlib.import_module(window_filename, package='vistool')
    window = None
    target_window_name = window_name.replace('_', '')
    for name, cls in windowlib.__dict__.items():
        if name.lower() == target_window_name.lower() \
            and issubclass(cls, BaseWindow):
            window = cls

    if window is None:
        print("In %s.py, there should be a subclass of BaseModel with class name that matches %s in lowercase." % (window_filename, target_window_name))
        exit(0)

    return window

