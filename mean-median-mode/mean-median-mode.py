from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    mean=np.mean(np.array(x))
    median=np.median(np.array(x))
    counts = Counter(x)
    highest_fre=max(counts.values())
    
    mode = min(value for value,count in counts.items() if count==highest_fre)
    return {'mean':float(mean),'median':float(median),'mode':float(mode)}