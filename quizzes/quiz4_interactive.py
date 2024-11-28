# Quiz 4: Interactive Object-Oriented Programming

# Import necessary libraries
import random

def multiple_choice_question(question, options, correct_answer):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    answer = input("Enter the number of your choice: ")
    return options[int(answer) - 1] == correct_answer

def coding_exercise(prompt, test_cases):
    print(prompt)
    user_code = input("Enter your code: ")
    for test_case in test_cases:
        if eval(user_code) != test_case['expected']:
            return False
    return True

# Questions
questions = [
    {
        'question': "What is a class in Python?",
        'options': ["A blueprint for creating objects", "A type of loop", "A function"],
        'correct_answer': "A blueprint for creating objects"
    },
    {
        'question': "How do you create an object from a class?",
        'options': ["Using the class name followed by parentheses", "Using a loop", "Using a function"],
        'correct_answer': "Using the class name followed by parentheses"
    }
]

# Coding Exercise
coding_prompt = "Write a class with a method that returns 'Hello, World!'."
test_cases = [
    {'input': None, 'expected': 'Hello, World!'}
]

# Run Quiz
score = 0
for q in questions:
    if multiple_choice_question(q['question'], q['options'], q['correct_answer']):
        score += 1

if coding_exercise(coding_prompt, test_cases):
    score += 1

print(f"Your score: {score}/{len(questions) + 1}")
