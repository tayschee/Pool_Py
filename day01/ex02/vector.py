import sys


class Vector():
    def __init__(self, init) :
        if (isinstance(init, list) == True) :
            self.values = [float(i) for i in init]
            self.size = init[-1] - init[0]
        elif (isinstance(init, int) == True) :
            self.size = init
            self.values = [float(i) for i in range(init)]
        elif (isinstance(init, tuple) == True) :
            self.size = init[1] - init[0]
            self.values = [float(init[0] + i) for i in range(self.size)]
        else :
            print("error")
            sys.exit()

    def __mul__(self, nb) :
        for i in range(self.size + 1):
            self.values[i] = float(self.values[i]) * nb
        return (self.values)
    def __radd__
        for
    def __str__(self) :
        return("Vector("+str(self.values))+")"
           
nb = Vector([0, 1, 2, 3])
nb = nb * 3
print(nb)
