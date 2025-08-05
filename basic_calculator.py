# Basic Calculator using Function Mapping

# Step 1: Define operation functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

# Step 2: Map operations to functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Step 3: Get user input
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    op = input("Enter the operation (+, -, *, /): ")

    # Step 4: Perform the operation
    if op in operations:
        result = operations[op](num1, num2)
        print(f"{num1} {op} {num2} = {result}")
    else:
        print("Invalid operation. Please use +, -, *, or /.")
except ValueError:
    print("Invalid input. Please enter numeric values.")
