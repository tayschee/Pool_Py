import sys


if (len(sys.argv) > 2):
    print("ERROR")
    sys.exit()
try :
    nb = int(sys.argv[1])
    if (nb == 0):
        print("I'm Zero")
    elif (nb % 2 == 0):
        print ("I'm Even")
    else:
        print ("I'm Odd")
except ValueError :
    print("ERROR")
