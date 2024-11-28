# Lesson 10: Classes and Objects in Python
# In this lesson, we will learn about classes and objects, which are fundamental concepts in object-oriented programming.

# What are Classes and Objects?
# Classes are blueprints for creating objects (instances).
# Objects are instances of classes that encapsulate data and functionality.

# Defining a Class
# Use the 'class' keyword to define a class.

# Example:
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")

# Creating an Object
# You can create an object by calling the class.

# Example:
my_dog = Dog("Buddy", 3)
print("My dog's name is", my_dog.name)
my_dog.bark()

# Adding Methods to a Class
# Methods are functions defined inside a class that operate on objects.

# Example:
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        print(f"The {self.make} {self.model} is starting.")

my_car = Car("Toyota", "Corolla")
my_car.start()

# Hands-On Exercises:
# 1. Define a class for a 'Book' with attributes like title and author, and a method to display book details.
# 2. Create objects of the 'Book' class and call the method to display details.
# 3. Experiment with adding more attributes and methods to the class.

# Try it Yourself!
# Practice defining classes and creating objects to understand object-oriented programming.

# Solution Example:
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#
#     def display_info(self):
#         print(f"Title: {self.title}, Author: {self.author}")
#
# my_book = Book("1984", "George Orwell")
# my_book.display_info()
