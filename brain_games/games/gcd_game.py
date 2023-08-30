from random import randint
from math import gcd


RULES = 'Find the greatest common divisor of given numbers.'


def question():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    return str(num1) + ' ' + str(num2), None


def game(question):
    num1 = int(question[0])
    num2 = int(question[1])

    return str(gcd(num1, num2))
