import math

from typing import List

def mean(samplelist: List):
    assert len(samplelist) > 0, "The list should not be empty"
    return round(sum(samplelist)/len(samplelist), 4)

def stddev(samplelist: List):
    med_arr = []
    list_mean = mean(samplelist)
    med_arr = [(x-list_mean)**2 for x in samplelist]
    return (sum(med_arr))**(1/2)

def correlation(sample1: List, sample2: List):

    # for denominator
    sample1stddev = stddev(sample1)
    sample2stddev = stddev(sample2)
    denominator = sample1stddev*sample2stddev

    # for numerator
    numerator=0.0
    
    sample1mean = mean(sample1)
    sample2mean = mean(sample2)

    for i in range(len(sample1)):
        numerator += (sample1[i]-sample1mean)*(sample2[i]-sample2mean)
    
    return numerator/denominator

def de_mean(xs: List[float]) -> List[float]:
    """Translate xs by subtracting its mean (result has mean 0)"""
    x_bar = mean(xs)
    return [x - x_bar for x in xs]

# The underscores indicate that these are "private" functions, as they're
# intended to be called by our median function but not by other people
# using our statistics library.
def _median_odd(xs: List[float]) -> float:
    """If len(xs) is odd, the median is the middle element"""
    return sorted(xs)[len(xs) // 2]

def _median_even(xs: List[float]) -> float:
    """If len(xs) is even, it's the average of the middle two elements"""
    sorted_xs = sorted(xs)
    hi_midpoint = len(xs) // 2  # e.g. length 4 => hi_midpoint 2
    return (sorted_xs[hi_midpoint - 1] + sorted_xs[hi_midpoint]) / 2

def median(v: List[float]) -> float:
    """Finds the 'middle-most' value of v"""
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)