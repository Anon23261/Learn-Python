# Lesson 5: Functions in Python
# In this lesson, we will learn about functions and how to use them to organize your code.

# What are Functions?
# Functions are blocks of code that perform a specific task. They help you organize your code and make it reusable.
# Functions can take inputs, perform actions, and return outputs.

# Defining a Function
# Use the 'def' keyword to define a function. You can specify parameters inside the parentheses.

# Example:
def greet():
    print("Hello, welcome to Python!")

# Calling a Function
# After defining a function, you can call it by using its name followed by parentheses.

greet()  # This will call the greet function and print the message.

# Functions with Parameters
# You can pass data to functions using parameters. This makes functions more flexible.

# Example:
def greet_person(name):
    print("Hello, " + name + "!")

# Calling the function with an argument
greet_person("Alice")

# Returning Values from Functions
# Functions can return values using the 'return' statement.

# Example:
def add_numbers(a, b):
    return a + b

# Call the function and store the result
result = add_numbers(3, 5)
print("The sum is:", result)

# Hands-On Exercises:
# 1. Define a function that takes two numbers as parameters and returns their product.
# 2. Create a function that checks if a number is even or odd and returns a corresponding message.
# 3. Experiment with functions that take multiple parameters and return different types of data.

# Try it Yourself!
# Define and call your own functions to perform various tasks.
# Use parameters and return values to make your functions flexible and reusable.

# Solution Example:
# def multiply_numbers(x, y):
#     return x * y
#
# product = multiply_numbers(4, 6)
# print("The product is:", product)
#
# def check_even_odd(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
#
# print(check_even_odd(7))
