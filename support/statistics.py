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