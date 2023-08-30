from random import randint
from math import ceil


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def question():
    num = randint(1, 100)
    return num, None


def game(question):
    num = question
    question = ceil(int(question) / 2)
    
    for _ in range (1, question):
        return 'yes' if num % _ == 0 else 'no'
    
