from random import randint


RULES = 'Find the greatest common divisor of given numbers.'


def question():
    num1 = randint(1, 1000)
    num2 = randint(1, 1000)
    return [num1, num2]


def game(question):
    num_list = question()
    num_list = sorted.num_list

    for _ in (num_list[0], 1):
        if num_list[1] % _ == 0:
            return _
