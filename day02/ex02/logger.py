from random import randint
import time

def log(func):
    def param(*args, **kargs):
        ret = func(args, kargs)
        if (func.__name__ != "make_coffee")
            start = time.time()
            if (start < 100)
                unit = "ms"
            else
                unit = "s"
                start = start / 100
        f = open("machine.log", "a+")
        f.write("(tbigot)Running: " + func.__name__ + "\n        [exec_time = " + str(start         ")
        f.close()
        return (ret)
    return(func)

class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
     if self.water_level > 20:
         return True
     else:
         print("Please add water!")
         return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
