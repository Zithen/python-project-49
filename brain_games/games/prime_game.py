from random import randint
from math import ceil


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def question():
    return randint(1, 100), None


def game(question):
    num = question
    question = ceil(int(question) / 2)

    for _ in range(question, 1, -1):
        if num % _ == 0:
            correct_answer = 'no'
            break
        else:
            correct_answer = 'yes'

    return correct_answer
