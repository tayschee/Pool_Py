from mean import mean

def variance(x):
    m = len(x)
    res = 0.0
    res_mean = mean(x)
    for i in x :
        res = res + (i - res_mean)**2
    return (res / m)
