# Lesson 14: Decorators in Python
# In this lesson, we will explore decorators, which allow you to modify the behavior of functions or classes.

# What are Decorators?
# Decorators are functions that wrap another function or method to modify its behavior.
# They are often used for logging, access control, and instrumentation.

# Function Decorators
# Use the '@' symbol to apply a decorator to a function.

# Example:
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Class Decorators
# Decorators can also be applied to classes to modify their behavior.

# Example:
class DecoratorClass:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Class decorator is called.")
        return self.func(*args, **kwargs)

@DecoratorClass
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# Hands-On Exercises:
# 1. Create a decorator that logs the execution time of a function.
# 2. Write a class decorator that modifies the return value of a function.
# 3. Experiment with applying multiple decorators to a single function.

# Try it Yourself!
# Practice using decorators to enhance the functionality of your code.

# Solution Example:
# import time
# def time_logger(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Execution time: {end_time - start_time} seconds")
#         return result
#     return wrapper
#
# @time_logger
# def slow_function():
#     time.sleep(2)
#     print("Function complete.")
#
# slow_function()
