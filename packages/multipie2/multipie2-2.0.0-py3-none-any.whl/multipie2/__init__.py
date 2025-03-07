import os

__version__ = "2.0.0"

# top directory ending with a separator.
__top_dir__ = os.path.normpath(os.path.join(os.path.dirname(__file__), "..")) + os.sep

DIGIT = 10  # digit for ndarray.
CHOP = 1e-10  # cut to zero.
TOL = 1e-11  # absolute tolerance.
