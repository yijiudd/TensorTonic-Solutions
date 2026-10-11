import numpy as np

def quantize_and_frame(data: list, decimals: int, pad_width: int) -> np.ndarray:
    """
    Returns float64 slices of rounded, floored, and ceiling-rounded values with zero borders.
    """
    np_data=np.array(data,dtype='float64')
    rounded=np.round(np_data,decimals)
    floored=np.floor(np_data)
    ceiled=np.ceil(np_data)
    pad_rounded=np.pad(rounded,pad_width,mode='constant',constant_values=0)
    pad_floored=np.pad(floored,pad_width,mode='constant',constant_values=0)
    pad_ceiled=np.pad(ceiled,pad_width,mode='constant',constant_values=0)
    return np.stack([pad_rounded,pad_floored,pad_ceiled])