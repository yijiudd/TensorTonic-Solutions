import numpy as np

def select_by_index(arr: list, indices: list, axis: int) -> np.ndarray:
    """
    Returns a 2D float64 array of the selected rows or columns.
    """
    np_data=np.array(arr,dtype='float64')
    return np.take(np_data,indices,axis=axis)
