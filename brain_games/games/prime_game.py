from random import randint
from math import ceil


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_logic():
    num = randint(1, 2)
    question = ceil(num / 2)
    # if num is 1 or 2 will avoid cycle
    correct_answer = 'no' if num == 1 else 'yes'

    for divisor in range(question, 1, -1):
        if num % divisor == 0:
            correct_answer = 'no'
            break
        else:
            correct_answer = 'yes'

    return str(num), correct_answer
