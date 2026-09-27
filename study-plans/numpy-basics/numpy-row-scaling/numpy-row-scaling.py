import numpy as np

def scale_rows(data: list, weights: list) -> np.ndarray:
    """
    Returns a float64 matrix with each row multiplied by its weight.
    """
    return np.array(data,dtype='float64')*np.array(weights,dtype='float64')[:,np.newaxis]
