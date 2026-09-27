import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    np_data=np.array(x)
    mean=np.mean(np_data)
    var=np.sum((np_data-mean)**2)/(len(x)-1)
    std=math.sqrt(var)
    return {'variance':float(var),'standard_deviation':float(std)}