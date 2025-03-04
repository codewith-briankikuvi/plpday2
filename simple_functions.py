def greet(name):
    print(f"Hello {name}!")

greet("Annah")
greet("Brian")
greet("Caleb")

def simple_calculator(operation, a, b):
    if operation == "add":
        print(a + b)
    elif operation == "subtract":
        print(a - b)
    elif operation == "multiply":
        print(a * b)
    elif operation == "divide":
        print(a / b)
    else:
        print("Invalid Operation")

simple_calculator("add", 5, 3)
simple_calculator("subtract", 5, 3)
simple_calculator("multiply", 5, 3)
simple_calculator("divide", 6, 3)
simple_calculator("modulus", 6, 3)