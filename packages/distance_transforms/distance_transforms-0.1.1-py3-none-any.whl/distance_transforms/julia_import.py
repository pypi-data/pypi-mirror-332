from juliacall import Main as jl

jl.seval("using Pkg; Pkg.status()")
jl.seval("using DLPack")
jl.seval("using CUDA")
jl.seval("using DistanceTransforms")

DLPack = jl.DLPack
DistanceTransforms = jl.DistanceTransforms

def is_cuda_available():
    """Check if CUDA is available in the Julia environment."""
    try:
        return bool(jl.CUDA.functional())
    except Exception:
        return False