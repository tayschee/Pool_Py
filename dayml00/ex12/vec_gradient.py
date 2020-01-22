import numpy as np

def vec_gradient(x, y, theta):
    return (((x.transpose()) * (np.dot(x, theta) - y)).mean(1))
