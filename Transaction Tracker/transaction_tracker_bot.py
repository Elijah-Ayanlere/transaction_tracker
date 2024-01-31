import json
import time
import sys
from difflib import get_close_matches


def load_transaction_tracker(file_path: str):
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data


def save_transaction_tracker(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, questions: list):
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None


def get_answer_for_question(question: str, transaction_tracker: dict):
    for q in transaction_tracker["question"]:
        if q["question"] == question:
            return q["answer"]


def chatbot():
    transaction_tracker: dict = load_transaction_tracker('transaction_tracker.json')

    while True:
        user_input: str = input('\nYou: ')

        if user_input.lower() == 'back':
            import transaction_tracker

        best_match: str | None = find_best_match(user_input, [q["question"] for q in transaction_tracker["question"]])

        if best_match:
            answer: str = get_answer_for_question(best_match, transaction_tracker)
            print(f"\nBot: {answer}")
        else:
            print('\nBot: I don\'t know the answer, can you teach me?')
            new_answer: str = input('\nType the answer or "skip" to skip: ')

            if new_answer.lower() != 'skip':
                transaction_tracker["question"].append({"question":user_input, "answer": new_answer})
                save_transaction_tracker('transaction_tracker.json', transaction_tracker)
                print('\nBot: Thank you! I learned a new response!')


chatbot()