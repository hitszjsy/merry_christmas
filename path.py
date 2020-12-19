import os.path as op
import sys

def get_resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        return op.join(sys._MEIPASS, relative_path)
    else:
        return op.join(op.abspath('.'), relative_path)