import json
import random
import time
from datetime import datetime

def load_questions():
    try:
        with open('questions.json', 'r') as f:
            return json.load(f).get('questions', [])
    except FileNotFoundError:
        return []

def run_quiz():
    questions = load_questions()
    if not questions:
        print('No questions found!')
        return
    random.shuffle(questions)
    score = 0
    for i, q in enumerate(questions, 1):
        print(f'Question {i}: {q[\
