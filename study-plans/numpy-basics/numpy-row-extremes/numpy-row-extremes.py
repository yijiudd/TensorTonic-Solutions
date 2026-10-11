import numpy as np

def row_extremes(data: list) -> np.ndarray:
    """
    Returns float64 rows of maxima, maximum indices, minima, and minimum indices.
    """
    np_data=np.array(data,dtype='float64')
    row_max=np_data.max(axis=1)
    max_index=np_data.argmax(axis=1)
    row_min=np_data.min(axis=1)
    min_index=np_data.argmin(axis=1)
    return np.stack([row_max,max_index,row_min,min_index])
