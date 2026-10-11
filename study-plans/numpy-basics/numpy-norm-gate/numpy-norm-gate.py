import numpy as np

def norm_gate(X: list, W: list, threshold: float) -> np.ndarray:
    """
    Returns an (n, k) float64 matrix of norm-gated transformed rows.
    """
    X_np=np.array(X,dtype='float64')
    W_np=np.array(W,dtype='float64')
    Z=X_np@W_np
    norm=np.linalg.norm(Z,axis=1)
    gate=norm>=threshold
    return Z*gate[:,None]
