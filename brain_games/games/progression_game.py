from random import randint


RULES = 'What number is missing in the progression?'


def game_logic():
    progression_first_elem = randint(1, 10)
    progression_list = [progression_first_elem]
    progression_step = randint(1, 10)
    element_to_hide = randint(0, 9)
    for _ in range(1, 10):
        progression_list.append(progression_list[_ - 1] + progression_step)

    answer = progression_list[element_to_hide]
    progression_list[element_to_hide] = '..'
    question_string = ' '.join(str(elem) for elem in progression_list)

    return question_string, str(answer)
