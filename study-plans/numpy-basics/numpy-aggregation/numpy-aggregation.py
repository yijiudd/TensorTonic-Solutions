import numpy as np

def summarize(data: list, axis: int) -> np.ndarray:
    """
    Returns float64 rows of mean, standard deviation, minimum, and maximum.
    """
    np_data=np.array(data,dtype='float64')
    mean=np.mean(np_data,axis)
    std=np.std(np_data,axis)
    min=np.min(np_data,axis)
    max=np.max(np_data,axis)
    return np.array([mean,std,min,max])