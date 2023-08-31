from random import randint


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_logic():
    number_for_question = randint(1, 1000)

    if number_for_question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return number_for_question, correct_answer
