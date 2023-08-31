from random import randint
from math import gcd


RULES = 'Find the greatest common divisor of given numbers.'


def game_logic():
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    nums_string = str(num1) + ' ' + str(num2)
    correct_answer = gcd(num1, num2)

    return nums_string, str(correct_answer)
