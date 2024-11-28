# Lesson 4: Loops in Python
# In this lesson, we will learn about loops and how to use them to repeat actions in your code.

# What are Loops?
# Loops allow you to execute a block of code multiple times. They are useful for tasks that require repetition.
# In Python, the main types of loops are 'for' loops and 'while' loops.

# The 'for' Loop
# The 'for' loop is used to iterate over a sequence (like a list, tuple, or string).
# It executes a block of code for each item in the sequence.

# Example:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# The 'while' Loop
# The 'while' loop repeats a block of code as long as a condition is true.
# It is useful when the number of iterations is not known beforehand.

# Example:
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1

# Nested Loops
# You can place one loop inside another loop. This is called a nested loop.

# Example:
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")

# Hands-On Exercises:
# 1. Use a 'for' loop to print each character in the string "Python".
# 2. Use a 'while' loop to print numbers from 10 to 1.
# 3. Create a nested loop to print a 3x3 grid of numbers.

# Try it Yourself!
# Modify the loops in the examples above to see different results.
# Use Python to create your own loops and explore the results.

# Solution Example:
# for char in "Python":
#     print(char)
#
# count = 10
# while count > 0:
#     print("Count is:", count)
#     count -= 1
#
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"i={i}, j={j}")
