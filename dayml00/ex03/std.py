import sys
from math import sqrt
sys.path.append('../ex02')
from variance import variance

def std(x):
    if (len(x) == 0):
        return (None)

    return(sqrt(variance(x)))
