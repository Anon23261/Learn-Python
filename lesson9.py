# Lesson 9: Exception Handling in Python
# In this lesson, we will learn how to handle errors and exceptions in Python.

# What are Exceptions?
# Exceptions are errors that occur during the execution of a program.
# They can disrupt the normal flow of a program, but they can be handled gracefully.

# Basic Exception Handling
# Use the 'try' and 'except' blocks to handle exceptions.

# Example:
try:
    result = 10 / 0  # This will cause a ZeroDivisionError
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# Handling Multiple Exceptions
# You can handle multiple exceptions by specifying different 'except' blocks.

# Example:
try:
    number = int("abc")  # This will cause a ValueError
except ValueError:
    print("Error: Invalid input. Please enter a number.")
except Exception as e:
    print("An unexpected error occurred:", e)

# The 'finally' Block
# The 'finally' block is executed no matter what, even if an exception occurs.

# Example:
try:
    file = open("example.txt", "r")
except FileNotFoundError:
    print("Error: File not found.")
finally:
    print("Execution completed.")

# Hands-On Exercises:
# 1. Write a program that prompts the user for a number and handles invalid input.
# 2. Create a program that opens a file and handles the case where the file does not exist.
# 3. Experiment with using 'finally' to ensure resources are released.

# Try it Yourself!
# Practice handling exceptions to make your programs more robust.

# Solution Example:
# try:
#     user_input = input("Enter a number: ")
#     number = int(user_input)
#     print("You entered:", number)
# except ValueError:
#     print("Error: Please enter a valid number.")
#
# try:
#     with open("myfile.txt", "r") as file:
#         content = file.read()
#         print("File Content:", content)
# except FileNotFoundError:
#     print("Error: The file does not exist.")
# finally:
#     print("File handling completed.")
