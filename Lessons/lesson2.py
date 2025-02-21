# Welcome to Lesson 2: Basic Arithmetic in Python
# In this lesson, we'll explore arithmetic operations and how to use them to perform calculations.

# Arithmetic Operations in Python
# Arithmetic operations are used to perform mathematical calculations.
# Python can be used as a powerful calculator to perform these operations.

# Addition (+)
# Adding two numbers together.
# This is the simplest form of arithmetic operation.
sum_result = 5 + 3  # Adds 5 and 3
print("Addition: 5 + 3 =", sum_result)

# Subtraction (-)
# Subtracting one number from another.
# This operation gives the difference between two numbers.
sub_result = 10 - 4  # Subtracts 4 from 10
print("Subtraction: 10 - 4 =", sub_result)

# Multiplication (*)
# Multiplying two numbers.
# This operation gives the product of two numbers.
mul_result = 6 * 7  # Multiplies 6 by 7
print("Multiplication: 6 * 7 =", mul_result)

# Division (/)
# Dividing one number by another.
# This operation gives the quotient.
div_result = 20 / 5  # Divides 20 by 5
print("Division: 20 / 5 =", div_result)

# Note: Be careful with division, as dividing by zero will cause an error.
try:
    div_by_zero_result = 10 / 0
    print("Division: 10 / 0 =", div_by_zero_result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# More Operations
# Python supports other operations like exponentiation and modulus.

# Exponentiation (**)
# Raising a number to the power of another.
exp_result = 2 ** 3  # 2 raised to the power of 3
print("Exponentiation: 2 ** 3 =", exp_result)

# Modulus (%)
# Finding the remainder after division.
mod_result = 10 % 3  # Remainder of 10 divided by 3
print("Modulus: 10 % 3 =", mod_result)

# Operator Precedence
# Python follows the standard mathematical order of operations (PEMDAS/BODMAS).
# Parentheses, Exponents, Multiplication/Division, Addition/Subtraction.
precedence_result = 5 + 3 * 2  # Multiplies 3 and 2 first, then adds 5
print("Precedence: 5 + 3 * 2 =", precedence_result)

# Hands-On Exercises:
# 1. Calculate the sum of 15 and 20 and print the result.
# 2. Subtract 8 from 50 and print the result.
# 3. Multiply 9 by 9 and print the result.
# 4. Divide 100 by 4 and print the result.
# 5. Calculate 5 raised to the power of 4 and print the result.
# 6. Find the remainder when 17 is divided by 5 and print it.
# 7. Experiment with operator precedence by creating complex expressions.

# Try it Yourself!
# Modify the numbers in the examples above to see different results.
# Use Python to perform your own calculations and explore the results.

# Solution Examples:
# sum_result = 15 + 20
# print("Sum: 15 + 20 =", sum_result)
# sub_result = 50 - 8
# print("Subtraction: 50 - 8 =", sub_result)
# mul_result = 9 * 9
# print("Multiplication: 9 * 9 =", mul_result)
# div_result = 100 / 4
# print("Division: 100 / 4 =", div_result)
# exp_result = 5 ** 4
# print("Exponentiation: 5 ** 4 =", exp_result)
# mod_result = 17 % 5
# print("Modulus: 17 % 5 =", mod_result)
# precedence_result = (5 + 3) * 2  # Parentheses change the order
# print("Precedence: (5 + 3) * 2 =", precedence_result)