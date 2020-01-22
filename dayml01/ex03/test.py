from mylinearregression import MyLinearRegression as MyLR
import numpy as np

X = np.array([[1., 1., 2., 3.], [5., 8., 13., 21.], [34., 55., 89.,
144.]])
Y = np.array([[23.], [48.], [218.]])
mylr = MyLR([[1.], [1.], [1.], [1.], [1]])
print(mylr.predict_(X))
print(mylr.cost_elem_(X,Y))
print(mylr.cost_(X,Y))
mylr.theta = mylr.fit_(X, Y, alpha = 1.6e-4, n_cycle=100000)
print(mylr.predict_(X))
print(mylr.cost_elem_(X,Y))
print(mylr.cost_(X,Y))
