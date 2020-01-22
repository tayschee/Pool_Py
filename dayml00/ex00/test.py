import numpy as np
from sum_ import sum_

X = np.array([0, 15, -9, 7, 12, 3, -21])
print(sum_(X, lambda x: x))
X = np.array([0, 15, -9, 7, 12, 3, -21])
print(sum_(X, lambda x: x**2))
