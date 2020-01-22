#import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

class ImageProcessor():

    def load(self, path):
        return(plt.imread(path))
    def display(self, array):
        plt.imshow(array)
        plt.show()
        pass
