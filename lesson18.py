# Lesson 18: Multithreading in Python
# In this lesson, we will explore multithreading, which allows concurrent execution of tasks in Python.

# What is Multithreading?
# Multithreading involves running multiple threads (smaller units of a process) simultaneously.
# It is useful for performing tasks concurrently, such as downloading files or handling multiple user requests.

# Using the threading Module
# Python provides the threading module to work with threads.

import threading
import time

# Creating a Simple Thread
# Example:
def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)

thread = threading.Thread(target=print_numbers)
thread.start()

# Joining Threads
# Use the join() method to wait for a thread to complete.

# Example:
thread.join()
print("Thread has finished execution.")

# Creating Multiple Threads
# Example:
def print_letters():
    for letter in ['A', 'B', 'C']:
        print(letter)
        time.sleep(1)

thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

# Hands-On Exercises:
# 1. Create a thread that performs a countdown from 10 to 1.
# 2. Implement a multithreaded program that downloads multiple files concurrently.
# 3. Experiment with thread synchronization using locks.

# Try it Yourself!
# Practice using threads to perform tasks concurrently in your code.

# Solution Example:
# def countdown(n):
#     while n > 0:
#         print("Countdown:", n)
#         n -= 1
#         time.sleep(1)
#
# countdown_thread = threading.Thread(target=countdown, args=(10,))
# countdown_thread.start()
# countdown_thread.join()
