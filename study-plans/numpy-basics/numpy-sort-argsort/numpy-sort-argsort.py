import numpy as np

def sort_with_indices(data: list, axis: int) -> np.ndarray:
    """
    Returns a (2, m, n) float64 array of sorted values and source indices.
    """
    np_data=np.array(data,dtype='float64')
    sorted=np.sort(np_data,axis)
    index=np.argsort(np_data,axis)
    return np.array([sorted,index])
