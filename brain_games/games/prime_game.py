from random import randint
from math import ceil


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_logic():
    num = randint(1, 20)
    question = ceil(int(num) / 2)

    for _ in range(question, 1, -1):
        if num % _ == 0:
            correct_answer = 'no'
            break
        else:
            correct_answer = 'yes'

    return num, correct_answer
