# Quiz 3: Interactive Data Structures

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
        'question': "What is a list in Python?",
        'options': ["A collection of ordered items", "A type of loop", "A function"],
        'correct_answer': "A collection of ordered items"
    },
    {
        'question': "How do you access an element in a tuple?",
        'options': ["Using an index", "Using a key", "Using a loop"],
        'correct_answer': "Using an index"
    }
]

# Coding Exercise
coding_prompt = "Write a function that returns the length of a list."
test_cases = [
    {'input': [1, 2, 3], 'expected': 3},
    {'input': [], 'expected': 0}
]

# Run Quiz
score = 0
for q in questions:
    if multiple_choice_question(q['question'], q['options'], q['correct_answer']):
        score += 1

if coding_exercise(coding_prompt, test_cases):
    score += 1

print(f"Your score: {score}/{len(questions) + 1}")
