import numpy as np

def predict_(theta, X):
    s = len(X)
    s2 = len(theta)
    mat = np.zeros(s, dtype=float)
    #print(X)
    X = np.insert(X, 0, 1, axis = 1)
    return(np.dot(X, theta))
 
