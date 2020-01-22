import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mylinearregression import MyLinearRegression as MyLR

data = pd.read_csv("../resources/are_blue_pills_magics.csv")
Xpill = np.array(data["Micrograms"]).reshape(-1,1)
Yscore = np.array(data["Score"]).reshape(-1,1)
lnm = MyLR(np.array([[12.0], [5.0]]))
print(lnm.theta)
lnm.fit_(Xpill, Yscore, n_cycle = 1000)
print(lnm.theta)
Ymodel1 = lnm.predict_(Xpill)

#Y_model1 = lnm.predict_(Xpill)

#print(Y_model1, "\n\n", Y_model2, "\n\n", Xpill, "\n\n", Yscore)

def linear_model1(predict, real, Xpill):
    
    plt.plot(Xpill, predict, "-+g", markersize=8, label="Spredict")
    plt.scatter(Xpill, real, s=26, c='turquoise', label='Strue')
    plt.xlabel("Quantity of blue pils (in micrograms)", fontsize=10)
    plt.ylabel("Space driving score", fontsize=10)
    plt.ylim(27, 82)
    plt.xlim(0.9, 6.7)
    plt.legend([predict, real])
    plt.grid()
    plt.show()

linear_model1(Ymodel1, Yscore, Xpill)
op_file = open("../resources/are_blue_pills_magics.csv", "r")

'''def vector_creation(op_file):

    data = pd.read_csv(op_file)
    Xpill = np.array(data["Micrograms"]).reshape(-1,1)
    Yscore = np.array(data["Score"]).reshape(-1,1)
    print(Xpill, "\n\n", Yscore)
    op_file.close()

vector_creation(op_file)'''
