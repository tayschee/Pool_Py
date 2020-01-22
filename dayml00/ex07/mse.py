import numpy as np

def mse(y, y_hat):
    nb = y.size
    if (nb != y_hat.size):
        return (None)
    res = 0.0
    for i in range(nb):
        res += (y_hat[i] - y[i]) ** 2
    return (res / nb)
        
