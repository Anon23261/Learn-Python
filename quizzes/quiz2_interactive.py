# Quiz 2: Interactive Functions and Modules

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
        'question': "How do you define a function in Python?",
        'options': ["def functionName():", "function functionName():", "create functionName()"],
        'correct_answer': "def functionName():"
    },
    {
        'question': "What is the purpose of a return statement?",
        'options': ["To exit a loop", "To return a value from a function", "To define a variable"],
        'correct_answer': "To return a value from a function"
    }
]

# Coding Exercise
coding_prompt = "Write a function that returns the sum of two numbers."
test_cases = [
    {'input': (2, 3), 'expected': 5},
    {'input': (10, 5), 'expected': 15}
]

# Run Quiz
score = 0
for q in questions:
    if multiple_choice_question(q['question'], q['options'], q['correct_answer']):
        score += 1

if coding_exercise(coding_prompt, test_cases):
    score += 1

print(f"Your score: {score}/{len(questions) + 1}")
