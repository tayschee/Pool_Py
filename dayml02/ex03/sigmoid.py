import numpy as np

def sigmoid_(x):
    if (isinstance(x, int) or isinstance(x, float)):
        return(1 / (1 + np.exp(-x)))
    else :
        s = len(x)
        for i in range(s):
           x[i] = 1 / (1 + np.exp(-x[i]))
    return (x)
