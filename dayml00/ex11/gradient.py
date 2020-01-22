import numpy as np

def gradient(x, y, theta):
    s = len(x)
    if (x.size == 0 or y.size == 0 or theta.size == 0 or len(x) != len(y) or len(x[0]) != len(theta)):
        return (None)
    delta = np.zeros(len(x[0]))
    for i in range(s) :
        delta += (np.dot(x[i], theta) - y[i]) * x[i]
    return(delta / s)
