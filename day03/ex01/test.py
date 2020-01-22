from imageProcessor import ImageProcessor
#import matplotlib.pyplot as plt

path = open("/Users/tbigot/POOL_py/day03/resources/42AI.png", "r")

r = ImageProcessor()

img = r.load("../resources/42AI.png")
r.display(img)
print(img)

#print(path)
#print(r.load)
