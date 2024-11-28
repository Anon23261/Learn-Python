# Quiz 6: Interactive Contact Book, Quiz Application, and Inventory System

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
        'question': "How do you store contacts in a contact book application?",
        'options': ["Using a dictionary", "Using a list", "Using a loop"],
        'correct_answer': "Using a dictionary"
    },
    {
        'question': "What data structure is suitable for storing quiz questions and answers?",
        'options': ["Dictionary", "List", "Tuple"],
        'correct_answer': "Dictionary"
    }
]

# Coding Exercise
coding_prompt = "Write a class that simulates a simple inventory system."
test_cases = [
    {'input': None, 'expected': 'Item added'}
]

# Run Quiz
score = 0
for q in questions:
    if multiple_choice_question(q['question'], q['options'], q['correct_answer']):
        score += 1

if coding_exercise(coding_prompt, test_cases):
    score += 1

print(f"Your score: {score}/{len(questions) + 1}")
