from random import randint


def even_game():
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    rand_num = randint(1, 1000)

    if rand_num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return {'rules': rules,
            'question': rand_num,
            'correct_answer': correct_answer}
