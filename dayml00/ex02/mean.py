import numpy as np

def mean(x) :
    m = len(x)
    res = 0.0
    for i in x :
        res = res + i
    return(res / m)

