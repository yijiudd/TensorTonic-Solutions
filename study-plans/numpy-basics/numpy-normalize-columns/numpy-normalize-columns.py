import numpy as np

def normalize(data: list) -> np.ndarray:
    """
    Returns a float64 matrix standardized independently by column.
    """
    np_data=np.array(data,dtype='float64')
    mean=np.mean(np_data,axis=0)
    theta=np.sqrt(np.mean(((np_data-mean)**2),axis=0))
    z=(np_data-mean)/theta
    return z
    
