# Project Module 4: Quiz Application

# Build a quiz application that presents multiple-choice questions.
# Utilize functions and control structures to manage the quiz flow.

# Example Code:

questions = {
    "What is the capital of France?": "a",
    "What is 2 + 2?": "b",
    "What is the color of the sky on a clear day?": "c"
}

options = [
    "a) Paris",
    "b) London",
    "c) Rome",
    "d) Berlin",
    "a) 3",
    "b) 4",
    "c) 5",
    "d) 6",
    "a) Green",
    "b) Red",
    "c) Blue",
    "d) Yellow"
]

def quiz():
    score = 0
    for i, (question, answer) in enumerate(questions.items()):
        print(question)
        for option in options[i*4:(i+1)*4]:
            print(option)
        user_answer = input("Your answer: ")
        if user_answer == answer:
            score += 1
    print(f"Your score: {score}/{len(questions)}")

quiz()
