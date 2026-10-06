import numpy as np

def angle_features(angles: list) -> np.ndarray:
    """
    Returns a (3, n) float64 array with sine, cosine, and tangent rows.
    """
    angle=np.array(angles,np.float64)
    sine=np.sin(angle)
    cosine=np.cos(angle)
    tangent=np.tan(angle)
    return np.row_stack([sine,cosine,tangent])
