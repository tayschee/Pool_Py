import numpy as np

def linear_mse(x, y, theta):
    s = len(x)
    if (s == 0 or len(y) == 0 or theta == 0 s != len(y) or theta.size != s):
        return (None)
    dotproduct = 0
    for i in range(s):
        dotproduct += (np.dot(theta, x[i]) - y[i]) ** 2
    return(dotproduct / s)
