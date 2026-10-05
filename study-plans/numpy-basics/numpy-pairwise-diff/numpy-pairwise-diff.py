import numpy as np

def pairwise_diff(a: list) -> np.ndarray:
    """
    Returns an (n, n) float64 array of signed pairwise differences.
    """
    a_np=np.array(a,dtype='float64')
    return a_np[:,None]-a_np[None,:]
