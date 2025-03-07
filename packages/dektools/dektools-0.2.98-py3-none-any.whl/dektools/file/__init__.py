from .path import *
from .re import *
from .operation import *

try:
    from .hit import *
except ImportError as e:
    if "'gitignore_parser'" in e.args[0]:
        pass
    else:
        raise
