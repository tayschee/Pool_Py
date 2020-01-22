import numpy as np

def mat_vec_prod(x, y):
    size = len(x)
    sizey = len(y)
    if (size == 0 or sizey == 0 or x[0].size != sizey):
        return (None)
    print(x, "\n", size, "\n\n", y, "\n", sizey)
    vec = np.zeros((size, 1), dtype=float)
    for i in range(size):
        for j in range(sizey):
            vec[i] = vec[i] + x[i][j] * y[j]
    return(vec)
