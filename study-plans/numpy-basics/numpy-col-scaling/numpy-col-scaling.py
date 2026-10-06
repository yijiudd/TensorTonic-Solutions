import numpy as np

def scale_cols(data: list, weights: list) -> np.ndarray:
    """
    Returns a float64 matrix with each column multiplied by its weight.
    """
    np_data=np.array(data,dtype="float64")
    np_weights=np.array(weights,dtype='float64')
    return np_data*np_weights
