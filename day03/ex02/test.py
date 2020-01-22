from ScrapBooker import ScrapBooker
import matplotlib.pyplot as plt


r = ScrapBooker()

#img = open("../resources/42AI.png", "")
imgn = plt.imread("../resources/small_img_1.png")
#plt.imshow(imgn)
#plt.show()

imgn = r.mosaic(imgn, (8, 8))
plt.imshow(imgn)
plt.show()
