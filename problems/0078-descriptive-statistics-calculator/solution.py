import numpy as np
import math

def compute_mean(data) -> float:
    ans = 0.0
    for num in data:
        ans += num
    
    return ans / len(data)

def compute_median(data) -> float:
    data.sort()
    n = len(data)
    if n % 2 == 0:
        return (data[n//2-1] + data[n//2]) / 2
    
    return data[n//2]

def compute_mode(data) -> float:
    hm = {}
    for num in data:
        if num in hm:
            hm[num] += 1
        else:
            hm[num] = 0
    
    ans, mx_count = data[0], 0
    for k, v in hm.items():
        if v > mx_count:
            ans = k
            mx_count = v
    
    return ans

def compute_var(data) -> float:
    ans = 0.0
    mean = compute_mean(data)

    for num in data:
        ans += (num-mean) ** 2
    
    return ans / len(data)



def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """

    q1, q2, q3 = np.percentile(np.array(data), [25, 50, 75])
    ans = dict({
        "mean": compute_mean(data),
        "median": compute_median(data),
        "mode": compute_mode(data),
        "variance": compute_var(data),
        "standard_deviation": math.sqrt(compute_var(data)),
        '25th_percentile': q1,
        '50th_percentile': q2,
        '75th_percentile': q3,
        "interquartile_range": q3-q1
    })
    return ans