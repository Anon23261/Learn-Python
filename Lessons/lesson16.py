# Lesson 16: Regular Expressions in Python
# In this lesson, we will explore regular expressions, which are used for pattern matching in strings.

# What are Regular Expressions?
# Regular expressions (regex) are sequences of characters that define search patterns.
# They are commonly used for string searching and manipulation.

# Using the 're' Module
# Python provides the 're' module to work with regular expressions.

import re

# Basic Pattern Matching
# Use 're.search()' to find a pattern in a string.

# Example:
text = "The rain in Spain"
match = re.search(r"rain", text)
if match:
    print("Pattern found:", match.group())

# Using Special Characters
# Special characters like '.', '*', and '?' have specific meanings in regex.

# Example:
pattern = r"r.n"
match = re.search(pattern, text)
if match:
    print("Pattern with special character found:", match.group())

# Compiling Regular Expressions
# Use 're.compile()' to compile a regex pattern for reuse.

# Example:
pattern = re.compile(r"Spain")
match = pattern.search(text)
if match:
    print("Compiled pattern found:", match.group())

# Hands-On Exercises:
# 1. Write a regex to find all words starting with 'S' in a given text.
# 2. Create a regex to validate email addresses.
# 3. Experiment with using regex to extract dates from a text.

# Try it Yourself!
# Practice using regular expressions to perform advanced string operations.

# Solution Example:
# text = "Send an email to example@example.com or support@example.org"
# email_pattern = r"[\w.-]+@[\w.-]+"
# emails = re.findall(email_pattern, text)
# print("Emails found:", emails)

# date_text = "Today's date is 2023-10-15"
# date_pattern = r"\d{4}-\d{2}-\d{2}"
# date_match = re.search(date_pattern, date_text)
# if date_match:
#     print("Date found:", date_match.group())
