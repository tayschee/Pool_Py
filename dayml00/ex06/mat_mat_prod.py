import numpy as np

def mat_mat_prod(x, y):
    row = len(x)
    column = len(y[0])
    igualsize = len(y)
    if (x == None or y == None or row == 0 or column == 0 or igualsize == 0 or igualsize != len(x[0])):
        return (None)
    print(row, column)
    mat = np.zeros((row, column), dtype=float)
    for i in range(row):
        for j in range(column):
            for k in range(igualsize):
                mat[i][j] += x[i][k] * y[k][j] 
    return(mat)
