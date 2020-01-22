import numpy as np

class ColorFilter :

    def invert(self, array):
        return(1 - array)

    def to_green(self, array):
        return ([0, 1, 0] * array)
