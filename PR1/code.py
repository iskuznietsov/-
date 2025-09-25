import math
from math import log10, cos, sin, sqrt

def task1_integer3 () :
    b = 1024
    try:
        i = int(input( "File size in bytes i = "))
    except:
        print("i must be an integer.")
        input("Press enter for exit ... ")
    else:
        # Тут можна додати блок if для того, щоб перевести 
        # число можна було не тільки в кілобайти.
        if i < b**2:
            result = i // b
            s = str ("KB")
            # Однак по суті на цьому етапі умова задачі виконана.
        else:
            result = i // (b**2)
            s = str ("MB")
        print(f'File size = {result} {s}')
task1_integer3()

def task2_31 () :
    try:
        x = float(input("Enter x = "))
    except:
        print("x must be a number.")
        input("Press enter for exit ... ")
    else:
        try:
            nom = float (log10(2*x**2+cos(37)))
            den = float (sqrt(abs(4-2*cos(x)-sin(x**2)**2)))
            y = float (nom/(sin(x**2)**3+den))
        except:
            print ("Calculation error.")
        else:
            print (f'y = {y}')
task2_31()

def task_boolean25():
    try:
        x = int(input("Enter x = "))
        y = int(input("Enter y = "))
    except:
        print("You must write an integer.")
    else:
        res = x < 0 and y > 0
        print(f"A point lies in the second quadrant: {res}")
task_boolean25()
