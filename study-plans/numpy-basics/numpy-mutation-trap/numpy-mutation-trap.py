import numpy as np

def original_and_clipped(data: list, row_idx: int, lo: float, hi: float) -> np.ndarray:
    """
    Returns a (2, n) float64 array: original row, then clipped row.
    """
    np_data=np.array(data,dtype='float64')
    original_row=np_data[row_idx,:]
    clipped=np.clip(original_row,lo,hi)
    return np.array([original_row,clipped])
