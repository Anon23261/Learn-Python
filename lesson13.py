# Lesson 13: Iterators and Generators in Python
# In this lesson, we will learn about iterators and generators, which provide efficient ways to iterate over data.

# What are Iterators?
# Iterators are objects that allow you to traverse through all the elements of a collection, one element at a time.
# An iterator implements two methods: __iter__() and __next__().

# Creating an Iterator
# Example:
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

my_iter = MyIterator([1, 2, 3])
for item in my_iter:
    print(item)

# What are Generators?
# Generators are a simple way to create iterators using functions and the 'yield' statement.
# They allow you to iterate over data without storing it in memory all at once.

# Creating a Generator
# Example:
def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)

# Hands-On Exercises:
# 1. Create a custom iterator that iterates over a list of strings and prints each string in uppercase.
# 2. Write a generator function that yields the first 10 even numbers.
# 3. Experiment with using generators to handle large datasets efficiently.

# Try it Yourself!
# Practice creating iterators and generators to efficiently handle data.

# Solution Example:
# class UpperCaseIterator:
#     def __init__(self, data):
#         self.data = data
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.data):
#             result = self.data[self.index].upper()
#             self.index += 1
#             return result
#         else:
#             raise StopIteration
#
# def even_numbers_generator():
#     num = 0
#     while num < 20:
#         yield num
#         num += 2
#
# for num in even_numbers_generator():
#     print(num)
