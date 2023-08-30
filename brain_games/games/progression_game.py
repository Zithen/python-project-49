from random import randint


RULES = 'What number is missing in the progression?'


def question():
    progression_first_elem = randint(1, 10000)
    progression_list = [progression_first_elem]
    progression_step = randint(1, 10000)
    for _ in range(1, 10):
        progression_list.append(progression_list[_ - 1] + progression_step)

    return ' '.join(str(elem) for elem in progression_list)


def game(question):
    return 1
