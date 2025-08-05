# Basic Calculator Program

# Ask the user to input the first number
num1 = float(input("Enter the first number: "))

# Ask the user to input the second number
num2 = float(input("Enter the second number: "))

# Ask the user to input the operation
operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operation entered. Please use +, -, *, or /.")
