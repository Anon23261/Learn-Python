# Lesson 19: Database Interaction in Python
# In this lesson, we will explore how to interact with databases using Python's SQLite module.

# What is SQLite?
# SQLite is a lightweight, disk-based database that doesn't require a separate server process.
# It is built into Python and provides a simple way to work with databases.

import sqlite3

# Connecting to a Database
# Use 'sqlite3.connect()' to connect to a database. If the database does not exist, it will be created.

# Example:
connection = sqlite3.connect('example.db')
cursor = connection.cursor()

# Creating a Table
# Use SQL commands to create tables and define their schema.

# Example:
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    age INTEGER
                )''')

# Inserting Data
# Use SQL commands to insert data into tables.

# Example:
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ('Alice', 21))
connection.commit()

# Querying Data
# Use SQL commands to query data from tables.

# Example:
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Closing the Connection
# Always close the connection when done.

# Example:
connection.close()

# Hands-On Exercises:
# 1. Create a new table for courses with columns for course name and credits.
# 2. Insert multiple records into the courses table and query them.
# 3. Experiment with updating and deleting records in the database.

# Try it Yourself!
# Practice using SQLite to interact with databases in your code.

# Solution Example:
# cursor.execute('''CREATE TABLE IF NOT EXISTS courses (
#                     id INTEGER PRIMARY KEY,
#                     name TEXT,
#                     credits INTEGER
#                 )''')
# cursor.execute("INSERT INTO courses (name, credits) VALUES (?, ?)", ('Math', 3))
# connection.commit()
# cursor.execute("SELECT * FROM courses")
# for row in cursor.fetchall():
#     print(row)
