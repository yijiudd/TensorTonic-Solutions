import numpy as np

def row_summary(data: list, threshold: float) -> np.ndarray:
    """
    Returns a float64 array of shape (3, m, n): mask, any-row, all-row.
    """
    np_data = np.array(data, dtype='float64')
    mask = np_data > threshold


    any_row = np.where(
        np.any(mask, axis=1, keepdims=True),
        np_data,
        0
    )

    all_row = np.where(
        np.all(mask, axis=1, keepdims=True),
        np_data,
        0
    )

    return np.stack([mask, any_row, all_row])