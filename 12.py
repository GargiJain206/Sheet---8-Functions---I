#Pythagoras Theorem
import math
def pythagoras(a, b):
    return math.sqrt(a*a + b*b)
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = pythagoras(a, b)
print("Hypotenuse =", c)
