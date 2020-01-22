def dot(x , y) :
    m = len(x)
    if (m == 0 or len(y) != m):
        return (None)
    res = 0.0
    for i in range(m) :
        res = res + x[i] * y[i]
    return(res)
