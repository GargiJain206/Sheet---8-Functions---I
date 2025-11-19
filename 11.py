# Calculator
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
ch = int(input("Enter your choice (1-4): "))
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
if ch == 1:
    print("Result:", add(a, b))
elif ch == 2:
    print("Result:", subtract(a, b))
elif ch == 3:
    print("Result:", multiply(a, b))
elif ch == 4:
    print("Result:", divide(a, b))
else:
    print("Invalid choice")
