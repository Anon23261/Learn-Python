# Lesson 6: Lists and Tuples in Python
# In this lesson, we will learn about lists and tuples, which are used to store collections of data.

# What are Lists?
# Lists are mutable sequences, which means you can change their content.
# They are defined using square brackets.

# Example:
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)

# Accessing List Elements
# You can access elements by their index (starting from 0).
print("First fruit:", fruits[0])

# Modifying List Elements
# You can change elements by assigning a new value to an index.
fruits[1] = "blueberry"
print("Modified Fruits:", fruits)

# What are Tuples?
# Tuples are immutable sequences, which means you cannot change their content.
# They are defined using parentheses.

# Example:
colors = ("red", "green", "blue")
print("Colors:", colors)

# Accessing Tuple Elements
# You can access elements by their index (starting from 0).
print("First color:", colors[0])

# Hands-On Exercises:
# 1. Create a list of your favorite movies and print it.
# 2. Modify the list to replace one movie with another and print the updated list.
# 3. Create a tuple of your favorite foods and print it.
# 4. Try accessing an element in the tuple and observe the result when attempting to modify it.

# Try it Yourself!
# Experiment with creating and modifying lists and tuples to understand their behavior.

# Solution Example:
# movies = ["Inception", "The Matrix", "Interstellar"]
# print("Movies:", movies)
#
# movies[1] = "The Godfather"
# print("Updated Movies:", movies)
#
# foods = ("pizza", "sushi", "tacos")
# print("Foods:", foods)
#
# print("First food:", foods[0])
# # Attempting to modify a tuple will result in an error
# # foods[0] = "pasta"  # Uncommenting this line will cause an error
