# Lesson 11: Inheritance and Polymorphism in Python
# In this lesson, we will explore inheritance and polymorphism, two key concepts in object-oriented programming.

# What is Inheritance?
# Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class).
# This promotes code reuse and logical hierarchy.

# Defining a Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Some generic animal sound")

# Defining a Child Class
# The child class inherits from the parent class and can override methods.
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says woof!")

# Creating an Object of the Child Class
my_dog = Dog("Buddy")
my_dog.speak()  # This will call the overridden method in Dog class

# What is Polymorphism?
# Polymorphism allows methods to do different things based on the object calling them.

# Example of Polymorphism
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says meow!")

animals = [Dog("Buddy"), Cat("Whiskers")]
for animal in animals:
    animal.speak()  # Calls the overridden method in each class

# Hands-On Exercises:
# 1. Define a class 'Bird' that inherits from 'Animal' and overrides the 'speak' method.
# 2. Create objects of 'Dog', 'Cat', and 'Bird' and call their 'speak' methods.
# 3. Experiment with adding more methods and attributes to the classes.

# Try it Yourself!
# Practice using inheritance and polymorphism to create flexible and reusable code.

# Solution Example:
# class Bird(Animal):
#     def speak(self):
#         print(f"{self.name} says tweet!")
#
# my_bird = Bird("Tweety")
# my_bird.speak()
