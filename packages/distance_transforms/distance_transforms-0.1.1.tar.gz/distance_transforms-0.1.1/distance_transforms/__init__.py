"""
Python bindings for the Julia DistanceTransforms.jl package.
"""

__version__ = "0.1.1"

from .julia_import import jl, DistanceTransforms
from .transform import transform

__all__ = [
    "jl",
    "DistanceTransforms",
    "transform",
]

# Only try to import transform_cuda if torch is available
try:
    from .transform_cuda import transform_cuda
    __all__.append("transform_cuda")
except ImportError:
    # CUDA functionality not available
    pass