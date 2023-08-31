from random import randint
from math import ceil


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_logic():
    num = randint(1, 20)
    question = ceil(num / 2)
    correct_answer = 'yes' # if num is 1 or 2 will avoid cycle

    for _ in range(question, 1, -1):
        if num % _ == 0:
            correct_answer = 'no'
            break
        else:
            correct_answer = 'yes'

    return str(num), correct_answer
