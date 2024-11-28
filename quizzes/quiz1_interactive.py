# Quiz 1: Interactive Basics of Programming and Control Structures

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
        'question': "What is a variable in programming?",
        'options': ["A storage location", "A type of loop", "A function"],
        'correct_answer': "A storage location"
    },
    {
        'question': "Which of the following is a data type in Python?",
        'options': ["integer", "loop", "function"],
        'correct_answer': "integer"
    }
]

# Coding Exercise
coding_prompt = "Write a function that returns the square of a number."
test_cases = [
    {'input': 2, 'expected': 4},
    {'input': 3, 'expected': 9}
]

# Run Quiz
score = 0
for q in questions:
    if multiple_choice_question(q['question'], q['options'], q['correct_answer']):
        score += 1

if coding_exercise(coding_prompt, test_cases):
    score += 1

print(f"Your score: {score}/{len(questions) + 1}")
