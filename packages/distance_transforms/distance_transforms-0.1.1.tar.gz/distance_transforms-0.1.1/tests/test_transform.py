"""
Tests for the distance_transforms package.
"""
import numpy as np
import pytest
from distance_transforms import transform

def test_transform_1d():
    """Test 1D distance transform."""
    # Create a 1D binary array with a single foreground point in the middle
    arr = np.zeros(11, dtype=np.uint8)
    arr[5] = 1
    
    # Compute distance transform
    result = transform(arr)
    
    # Expected squared distances: [25, 16, 9, 4, 1, 0, 1, 4, 9, 16, 25]
    expected = np.array([25, 16, 9, 4, 1, 0, 1, 4, 9, 16, 25], dtype=np.float32)
    
    np.testing.assert_allclose(result, expected, rtol=1e-5)

def test_transform_2d():
    """Test 2D distance transform."""
    # Create a 5x5 binary array with a single foreground point in the center
    arr = np.zeros((5, 5), dtype=np.uint8)
    arr[2, 2] = 1
    
    # Compute distance transform
    result = transform(arr)
    
    # Expected squared distances
    expected = np.array([
        [8, 5, 4, 5, 8],
        [5, 2, 1, 2, 5],
        [4, 1, 0, 1, 4],
        [5, 2, 1, 2, 5],
        [8, 5, 4, 5, 8]
    ], dtype=np.float32)
    
    np.testing.assert_allclose(result, expected, rtol=1e-5)

@pytest.mark.skip("Only run this test if CUDA is available")
def test_transform_cuda():
    """Test CUDA distance transform if available."""
    try:
        import torch
        from distance_transforms import transform_cuda
        
        # Skip if CUDA not available
        if not torch.cuda.is_available():
            pytest.skip("CUDA not available")
            
        # Create a binary tensor on GPU
        tensor = torch.zeros((5, 5), dtype=torch.bool, device="cuda")
        tensor[2, 2] = True
        
        # Compute distance transform
        result = transform_cuda(tensor)
        
        # Expected squared distances
        expected = torch.tensor([
            [8, 5, 4, 5, 8],
            [5, 2, 1, 2, 5],
            [4, 1, 0, 1, 4],
            [5, 2, 1, 2, 5],
            [8, 5, 4, 5, 8]
        ], dtype=torch.float32, device="cuda")
        
        torch.testing.assert_close(result, expected, rtol=1e-5)
        
    except ImportError:
        pytest.skip("PyTorch not installed")