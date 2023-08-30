from random import randint


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def question():
    return randint(1, 1000), None


def game(question):
    rand_num = question

    if rand_num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return correct_answer
