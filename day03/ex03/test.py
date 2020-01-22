from ColorFilter import ColorFilter
import numpy as np
import matplotlib.pyplot as plt

r = ColorFilter()
img = plt.imread("../resources/42AI.png")
plt.imshow(img)
plt.show()
imgn = r.to_green(img)
print(imgn)
plt.imshow(imgn)
plt.show()


