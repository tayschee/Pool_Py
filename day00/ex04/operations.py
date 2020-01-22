import sys


def operator(v1, v2) :
    try :
        a = int(v1)
        b = int(v2)
    except ValueError :
        print("InputError: only numbers")
    print ("Sum:", a + b)
    print ("Difference:", a - b)
    print ("Product:", a * b)
    try :
        print ("Quotient:", a / b)
        print ("Remainder:", a % b)
    except ZeroDivisionError:
        print ("ERROR (div by zero)")
        print ("ERROR (modulo by zero)")

operator(sys.argv[1], sys.argv[2])
