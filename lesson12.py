# Lesson 12: Modules and Packages in Python
# In this lesson, we will learn about modules and packages, which help organize and reuse code in Python.

# What are Modules?
# Modules are files containing Python code that can define functions, classes, and variables.
# They help organize code into reusable components.

# Importing a Module
# Use the 'import' statement to include a module in your code.

# Example:
import math

# Using a Module
# Access functions and variables defined in a module using dot notation.
print("Square root of 16:", math.sqrt(16))

# Creating a Custom Module
# You can create your own modules by writing Python code in a file and saving it with a .py extension.

# Example: Create a file named 'mymodule.py' with the following content:
# def greet(name):
#     print(f"Hello, {name}!")

# Import and use the custom module:
# import mymodule
# mymodule.greet("Alice")

# What are Packages?
# Packages are directories containing multiple modules and a special __init__.py file.
# They help organize modules into a hierarchy of directories.

# Creating a Package
# Example structure:
# mypackage/
#     __init__.py
#     module1.py
#     module2.py

# Importing from a Package
# Use dot notation to import specific modules from a package.
# from mypackage import module1

# Hands-On Exercises:
# 1. Create a custom module with a function and import it into another script.
# 2. Organize multiple modules into a package and import them using dot notation.
# 3. Explore built-in Python modules and use their functions in your code.

# Try it Yourself!
# Practice creating and using modules and packages to organize your code.

# Solution Example:
# # Create a file named 'mymodule.py'
# def add(a, b):
#     return a + b
#
# # In another script
# import mymodule
# print("Sum:", mymodule.add(3, 5))
