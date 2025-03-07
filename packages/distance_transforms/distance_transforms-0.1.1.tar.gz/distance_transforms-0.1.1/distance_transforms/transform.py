"""
CPU implementation of distance transform using NumPy arrays.
"""
import numpy as np
from .julia_import import jl, DistanceTransforms

def transform(arr):
    """
    Compute the squared Euclidean distance transform of a binary array.
    
    Parameters
    ----------
    arr : numpy.ndarray
        Input binary array where non-zero values represent the foreground.
        
    Returns
    -------
    numpy.ndarray
        Array of the same shape as input containing the squared Euclidean
        distance from each pixel to the nearest non-zero pixel.
    """
    # Convert NumPy array to Julia array
    arr_jl = jl.convert(jl.Array, arr)
    
    # Apply boolean indicator and then transform
    result_jl = DistanceTransforms.transform(DistanceTransforms.boolean_indicator(arr_jl))
    
    # Convert back to NumPy array
    return np.asarray(result_jl, dtype=np.float32)