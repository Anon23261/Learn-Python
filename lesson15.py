# Lesson 15: Context Managers in Python
# In this lesson, we will explore context managers, which provide a way to manage resources efficiently.

# What are Context Managers?
# Context managers are used to properly manage resources like files or network connections.
# They ensure that resources are acquired and released properly.

# Using the 'with' Statement
# The 'with' statement is used to wrap the execution of a block of code with methods defined by a context manager.

# Example:
with open("example.txt", "w") as file:
    file.write("Hello, world!\n")
# The file is automatically closed when the block is exited.

# Creating a Custom Context Manager
# You can create a custom context manager using a class that implements __enter__ and __exit__ methods.

# Example:
class MyContextManager:
    def __enter__(self):
        print("Entering the context.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context.")

with MyContextManager() as manager:
    print("Inside the context.")

# Hands-On Exercises:
# 1. Create a custom context manager that logs the time taken to execute a block of code.
# 2. Use a context manager to manage a database connection.
# 3. Experiment with using context managers to handle other resources like network connections.

# Try it Yourself!
# Practice using context managers to efficiently manage resources in your code.

# Solution Example:
# import time
# class Timer:
#     def __enter__(self):
#         self.start_time = time.time()
#         return self
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         end_time = time.time()
#         print(f"Elapsed time: {end_time - self.start_time} seconds")
#
# with Timer() as timer:
#     # Simulate a long-running operation
#     time.sleep(2)
