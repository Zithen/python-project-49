from random import randint


RULES = 'What number is missing in the progression?'


def game_logic():
    prog_first_elem = randint(1, 10)
    prog_list = [prog_first_elem]
    prog_step = randint(1, 10)
    element_to_hide = randint(0, 9)
    for prog_element in range(1, 10):
        prog_list.append(prog_list[prog_element - 1] + prog_step)

    answer = prog_list[element_to_hide]
    prog_list[element_to_hide] = '..'
    question_string = ' '.join(str(elem) for elem in prog_list)

    return question_string, str(answer)
