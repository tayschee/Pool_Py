import numpy as np

def log_loss_(y_true, y_pred, m, eps=1e-15):
    if isinstance(y_pred, float or isinstance(y_pred, int)):
        return((-1 / m) * (y_true * np.log(y_pred + eps) + (1 - y_true) * np.log(1 - y_pred + eps)))
    res = 0
    for i in range(m):
        res += y_true[i] * np.log(y_pred[i] + eps) + (1 - y_true[i]) * np.log(1 - y_pred[i] + eps)
    return((-1 / m) * res)
