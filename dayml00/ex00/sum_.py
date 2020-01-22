import numpy as np

def  sum_(x, f) :
    res = 0.0
    for i in x :
        res = res + f(i)
    return(res)


