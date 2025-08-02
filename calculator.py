# This program asks for two numbers and an operation, then shows the result
# Ask user for first number
num1 = float(input("Enter first number: "))

# Ask user for second number  
num2 = float(input("Enter second number: "))

# Ask user for operation
operation = input("Enter operation (+, -, *, /): ")

# Do the calculation and show result
if operation == "+":
    result = num1 + num2
    print(num1, "+", num2, "=", result)

elif operation == "-":
    result = num1 - num2
    print(num1, "-", num2, "=", result)

elif operation == "*":
    result = num1 * num2
    print(num1, "*", num2, "=", result)

elif operation == "/":
    result = num1 / num2
    print(num1, "/", num2, "=", result)

else:
    print("Invalid operation!")