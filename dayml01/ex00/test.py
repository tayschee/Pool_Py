from pred import predict_
import numpy as np

X = np.array([[0.], [1.], [2.], [3.], [4.]])
theta = np.array([[2.], [4.]])
print(predict_(theta, X))
#X3 = np.array([[0.2, 2., 20.], [0.4, 4., 40.], [0.6, 6., 60.], [0.8, 8.,
#80.]])
#theta3 = np.array([[0.05], [1.], [1.], [1.]])
#print(predict_(theta3, X3))
