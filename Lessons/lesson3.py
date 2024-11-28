# Lesson 3: Conditional Statements in Python
# In this lesson, we will learn about conditional statements and how to use them to make decisions in your code.

# What are Conditional Statements?
# Conditional statements allow you to execute certain parts of your code based on conditions. They help you make decisions.
# In Python, the main conditional statements are 'if', 'else', and 'elif'.

# The 'if' Statement
# The 'if' statement executes a block of code if a specified condition is true.
# If the condition is false, the code block is skipped.

# Example:
number = 10
if number > 5:
    print("The number is greater than 5.")

# The 'else' Statement
# The 'else' statement executes a block of code if the condition in the 'if' statement is false.
# It provides an alternative action when the 'if' condition is not met.

# Example:
number = 3
if number > 5:
    print("The number is greater than 5.")
else:
    print("The number is not greater than 5.")

# The 'elif' Statement
# The 'elif' statement allows you to check multiple conditions.
# It stands for 'else if' and can be used to add additional conditions to check.

# Example:
number = 5
if number > 5:
    print("The number is greater than 5.")
elif number == 5:
    print("The number is equal to 5.")
else:
    print("The number is less than 5.")

# Hands-On Exercises:
# 1. Write a program to check if a number is positive, negative, or zero.
# 2. Create a program to determine if a person is a child, teenager, or adult based on their age.
# 3. Experiment with nested 'if' statements to create more complex decision-making logic.

# Try it Yourself!
# Change the value of 'number' in the examples above and observe the output.
# Create your own conditions and print different messages based on those conditions.

# Solution Example:
# number = -10
# if number > 0:
#     print("The number is positive.")
# elif number < 0:
#     print("The number is negative.")
# else:
#     print("The number is zero.")
#
# age = 16
# if age < 13:
#     print("Child")
# elif age < 20:
#     print("Teenager")
# else:
#     print("Adult")
