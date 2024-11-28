# Lesson 7: Dictionaries in Python
# In this lesson, we will learn about dictionaries, which are used to store data in key-value pairs.

# What are Dictionaries?
# Dictionaries are mutable collections that store data in key-value pairs.
# They are defined using curly braces.

# Example:
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}
print("Student:", student)

# Accessing Dictionary Elements
# You can access values by their keys.
print("Name:", student["name"])

# Modifying Dictionary Elements
# You can change values by assigning a new value to a key.
student["age"] = 21
print("Updated Student:", student)

# Adding New Key-Value Pairs
# You can add new key-value pairs to a dictionary.
student["graduation_year"] = 2023
print("Extended Student:", student)

# Hands-On Exercises:
# 1. Create a dictionary for a book with keys like title, author, and year, and print it.
# 2. Update the year of the book and add a new key for the genre.
# 3. Create a dictionary for a car with keys like make, model, and year, and print it.
# 4. Access and print the model of the car.

# Try it Yourself!
# Experiment with creating and modifying dictionaries to understand their behavior.

# Solution Example:
# book = {
#     "title": "1984",
#     "author": "George Orwell",
#     "year": 1949
# }
# print("Book:", book)
#
# book["year"] = 1950
# book["genre"] = "Dystopian"
# print("Updated Book:", book)
#
# car = {
#     "make": "Toyota",
#     "model": "Corolla",
#     "year": 2020
# }
# print("Car:", car)
#
# print("Car Model:", car["model"])
