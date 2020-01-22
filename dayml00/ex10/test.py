import numpy as np
from vec_linear_mse import vec_linear_mse

X = np.array([ 
        [ -7, -9],
        [ -2, 14],
        [ 14, -1],
        [ -4, 6],
        [-9, 6],
        [-5, 11],
        [-11, 8]])
Y = np.array([2, 14, -13, 5, 12, 4, -19])
Z = np.array([0.5,-6])
print(vec_linear_mse(X, Y, Z))
