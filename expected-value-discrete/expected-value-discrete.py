import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    x=np.array(x,dtype='float64')
    p=np.array(p,dtype='float64')
    exp=np.sum(x*p)
    # Write code here
    return exp