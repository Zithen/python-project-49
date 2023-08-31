from random import randint
from math import ceil


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_logic():
    num = randint(1, 3571)
    # no sense to check num / > half of num as it will give remainder
    upper_limit_divisor = ceil(num / 2)
    # if num is 1 or 2 will avoid cycle below and miss the returned var value
    correct_answer = 'no' if num == 1 else 'yes'

    for divisor in range(upper_limit_divisor, 1, -1):
        if num % divisor == 0:
            correct_answer = 'no'
            break
        else:
            correct_answer = 'yes'

    return str(num), correct_answer
