import numpy as np

def reshape_array(data: list, operation: str) -> np.ndarray:
    """
    Returns a float64 array with the shape selected by operation.
    """
    np_data=np.array(data,dtype='float64')
    if operation=='flatten':
        return np_data.flatten()
    elif operation=='transpose':
        return np_data.T
    elif operation=='add_batch':
        return np.expand_dims(np_data,axis=0)

