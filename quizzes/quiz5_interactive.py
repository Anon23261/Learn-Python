# Quiz 5: Interactive Calculator and Guessing Game

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
        'question': "What is the purpose of using random numbers in a guessing game?",
        'options': ["To generate a random target number", "To control the game flow", "To display messages"],
        'correct_answer': "To generate a random target number"
    },
    {
        'question': "How do you handle division by zero in a calculator?",
        'options': ["By checking if the divisor is zero", "By using a loop", "By using a random number"],
        'correct_answer': "By checking if the divisor is zero"
    }
]

# Coding Exercise
coding_prompt = "Write a function that simulates a simple guessing game."
test_cases = [
    {'input': None, 'expected': 'Correct!'}
]

# Run Quiz
score = 0
for q in questions:
    if multiple_choice_question(q['question'], q['options'], q['correct_answer']):
        score += 1

if coding_exercise(coding_prompt, test_cases):
    score += 1

print(f"Your score: {score}/{len(questions) + 1}")
