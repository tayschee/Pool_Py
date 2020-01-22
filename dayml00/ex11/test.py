from gradient import gradient
import numpy as np
X = np.array([
    [ -7, -9],
        [ -2, 14],
        [ 4, -1],
        [ 4, 6],
        [ -9, 6],
        [ -5, 11],
        [ -11, 8]])
Y = np.array([2, 14, -13, 5, 12, 4])
Z = np.array([3,0.5])

print(gradient(X, Y, Z))
