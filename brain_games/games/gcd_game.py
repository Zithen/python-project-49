from random import randint
from math import gcd


RULES = 'Find the greatest common divisor of given numbers.'


def question():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    return str(num1) + ' ' + str(num2), None


def game(question):
    nums_list_final = []
    nums_list = question.split()

    for _ in nums_list:
        nums_list_final.append(int(_))

    return str(gcd(nums_list_final))
