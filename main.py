
# A simple calculator with a bug in the multiply function

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    # Bug: multiply is implemented as addition
    return a + b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

if __name__ == "__main__":
    print("Calculator Functions")
    print("Addition: 2 + 3 =", add(2, 3))
    print("Subtraction: 5 - 2 =", subtract(5, 2))
    print("Multiplication: 4 * 3 =", multiply(4, 3))  # This will show the bug
    print("Division: 10 / 2 =", divide(10, 2))
