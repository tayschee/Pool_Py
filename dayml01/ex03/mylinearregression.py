import numpy as np

class MyLinearRegression():
    def __init__(self, theta):
        self.theta = theta
    def predict_(self, X):
        mat = np.zeros(len(X), dtype=float)
        X = np.insert(X, 0, 1, axis = 1)
        return(np.dot(X, self.theta))

    def cost_elem_(self, X, Y):
        X = np.insert(X, 0, 1, axis = 1)
        return(((np.dot(X, self.theta) - Y) ** 2) / (2 * len(X)))

    def cost_(self, X, Y):
        vec = self.cost_elem_(X, Y)
        return(float(sum(vec)))

    def fit_(self, X, Y, alpha = 1, n_cycle = 2000):
        n_tet = self.theta
        X = np.insert(X, 0, 1, axis = 1)
        for i in range(1, n_cycle):
            n_tet -= alpha * (np.dot(X.transpose(), (np.dot(X, n_tet) - Y))) / (2 * len(X))
        return(n_tet)
