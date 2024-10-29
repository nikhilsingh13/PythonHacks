import math

def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=1e-5):
    """Find approximate inverse using binary search"""

    # if not standard, compute standard and rescale
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

    low_z, low_p = -10.0, 0           # lower bounds in z and p
    hi_z, hi_p = 10.0, 1              # upper bounds in z and p
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2    # midpoint in z
        mid_p = math.erf(mid_z / math.sqrt(2)) / 2 + 0.5  # midpoint in p using the error function
        if mid_p < p:
            low_z, low_p = mid_z, mid_p
        else:
            hi_z, hi_p = mid_z, mid_p

    return mid_z