import numpy as np

class LogisticRegressionBatchGd:

    

    def __init__(self, alpha=0.001, max_iter=1000, verbose=False, learning_rate='constant'):
        self.alpha = alpha
        self.max_iter = max_iter
        self.verbose = verbose
        self.learning_rate = learning_rate
        self.thetas = []

    def predict(self, x):
        if (isinstance(x, int) or isinstance(x, float)):
            return (round((1 / (1 + np.exp(-x)) > 5)))
        else :
            s = len(x)
            for i in range(s):
                x[i] = round(1 / (1 + np.exp(-x[i])))
        return (x)

    def fit(self, x_train, y_train):
        y_fit = self.predict(x_train)
            for i in range(max_iter)
                y_fit = alpha * self.predict(x_train)


    def score(self, x_train, y_train):
        pass
