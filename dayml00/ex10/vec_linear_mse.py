import numpy as np

def vec_linear_mse(x, y, theta):
    if (x.size == 0 or y.size == 0 or theta.size == 0 or len(x) != len(y) or len(x[0]) != len(theta)):
        return (None)
    return (((np.dot(x, theta) - y).transpose() * (np.dot(x, theta) - y)).mean())
