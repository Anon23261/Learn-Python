# Lesson 8: File Handling in Python
# In this lesson, we will learn how to read from and write to files using Python.

# Opening a File
# Use the 'open' function to open a file. You can specify the mode: 'r' for reading, 'w' for writing, 'a' for appending.

# Example:
file = open("example.txt", "w")  # Opens the file in write mode
file.write("Hello, world!\n")  # Writes to the file
file.close()  # Closes the file

# Reading from a File
# Use the 'read' method to read the contents of a file.

# Example:
file = open("example.txt", "r")  # Opens the file in read mode
content = file.read()  # Reads the entire file
print("File Content:", content)
file.close()

# Using 'with' Statement
# The 'with' statement is used for better file handling. It automatically closes the file.

# Example:
with open("example.txt", "a") as file:  # Opens the file in append mode
    file.write("Appending a new line.\n")

with open("example.txt", "r") as file:  # Opens the file in read mode
    for line in file:
        print("Line:", line.strip())

# Hands-On Exercises:
# 1. Create a new file and write a few lines of text to it.
# 2. Read the contents of the file and print each line.
# 3. Append additional text to the file and read it again.

# Try it Yourself!
# Experiment with file operations to understand how to manage files in Python.

# Solution Example:
# with open("myfile.txt", "w") as file:
#     file.write("This is a test file.\n")
#     file.write("It contains multiple lines.\n")
#
# with open("myfile.txt", "r") as file:
#     for line in file:
#         print("Line:", line.strip())
#
# with open("myfile.txt", "a") as file:
#     file.write("Adding more content.\n")
#
# with open("myfile.txt", "r") as file:
#     for line in file:
#         print("Updated Line:", line.strip())
