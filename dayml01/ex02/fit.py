import numpy as np
import sys
sys.path.insert(1, '../ex01')
from cost_function import cost_

def fit_(theta, X, Y, alpha=1, n_cycle=200):
    X = np.insert(X, 0, 1, axis = 1)
    for i in range(1, n_cycle):
        theta -= alpha * (np.dot(X.transpose(), (np.dot(X, theta) - Y))) / ( 2 * len(X))
    return(theta)

    
