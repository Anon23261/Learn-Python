# Project Module 1: Basic Calculator

# Create a simple calculator that can perform basic arithmetic operations.
# Focus on using functions and handling user input.

# Example Code:

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

operation = input("Choose an operation (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operation == '+':
    print(f"Result: {add(num1, num2)}")
elif operation == '-':
    print(f"Result: {subtract(num1, num2)}")
elif operation == '*':
    print(f"Result: {multiply(num1, num2)}")
elif operation == '/':
    print(f"Result: {divide(num1, num2)}")
else:
    print("Invalid operation")
