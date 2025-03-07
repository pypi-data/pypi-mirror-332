"""
CUDA implementation of distance transform using PyTorch tensors.
"""
import torch
from .julia_import import DLPack, DistanceTransforms, is_cuda_available

def transform_cuda(tensor):
    """
    Compute the squared Euclidean distance transform of a binary tensor on CUDA.
    
    Parameters
    ----------
    tensor : torch.Tensor
        Input binary tensor where non-zero values represent the foreground.
        Must be on a CUDA device.
        
    Returns
    -------
    torch.Tensor
        Tensor of the same shape as input containing the squared Euclidean
        distance from each element to the nearest non-zero element.
        
    Raises
    ------
    RuntimeError
        If CUDA is not available or the input tensor is not on a CUDA device.
    """
    if not is_cuda_available():
        raise RuntimeError("CUDA not available in the Julia environment.")
    
    if not tensor.is_cuda:
        raise RuntimeError("Input tensor must be on a CUDA device.")
    
    # Convert PyTorch tensor to Julia array via DLPack
    tensor_jl = DLPack.from_dlpack(tensor)
    
    # Apply boolean indicator and then transform
    result_jl = DistanceTransforms.transform(DistanceTransforms.boolean_indicator(tensor_jl))
    
    # Convert back to PyTorch tensor
    return DLPack.share(result_jl, torch.from_dlpack)