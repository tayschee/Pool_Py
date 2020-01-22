import matplotlib.pyplot as plt
import numpy as np


class   ScrapBooker():

    def crop(self, array, dimension, position = (0, 0)):
        print(position)
        print(dimension)
        return(array[position[0] : dimension[0], position[1] : dimension[1]])

    def thin(self, array, n, axis):
        return(np.delete(array, np.s_[::n], axis))
        
    def juxtapose(self, array, n, axis):
        new = array
        for i in range(n - 1):
            new = np.concatenate((new, array), axis)
        return (new)

    def mosaic(self, array, dimensions):
        newarray = self.juxtapose(array, dimensions[1], 1)
        print(newarray)
        return(self.juxtapose(newarray, dimensions[0], 0))
        
