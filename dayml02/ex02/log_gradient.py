def log_gradient_(x, y_true, y_pred):
    if not (isinstance(y_true, float) or isinstance(y_true, int)):
        m = len(y_true)
        s = len(x[0])
        res = [0 for i in range(s)]
        for i in range(s):
            for j in range(m):
                res[i] += (y_pred[j] - y_true[j]) * x[j][i]
        return(res)
    else :
        s = len(x)
        res = [0 for i in range(s)]
        for i in range(s):
            res[i] = (y_pred - y_true) * x[i]
        return(res)
