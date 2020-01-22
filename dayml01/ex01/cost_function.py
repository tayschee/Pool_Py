import numpy as np

def cost_elem_(theta, X, Y):
    X = np.insert(X, 0, 1, axis = 1)
    return(((np.dot(X, theta) - Y) ** 2) / (2 * len(X)))
    

def cost_(theta, X, Y):
    vec = cost_elem_(theta, X, Y)
    return(float(sum(vec)))
