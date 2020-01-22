import numpy as np

def vec_mse(y, y_hat):
    if (y.size != y_hat.size or y.size == 0 or y_hat.size == 0):
        return (None)
    return(np.square(y_hat - y).mean())
