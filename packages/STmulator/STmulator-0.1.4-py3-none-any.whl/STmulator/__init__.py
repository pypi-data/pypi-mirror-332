__version__ = "0.1.4"

# Import key components to make them available at the top level
from STmulator.STmulator_core import simulator
from STmulator.interpolation import interpolation_pipe

__all__ = ["simulator", "interpolation_pipe"]