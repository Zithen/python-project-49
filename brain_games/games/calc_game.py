from random import randint, choice


RULES = 'What is the result of the expression?'


def game_logic():
    operand1 = randint(1, 10)
    operand2 = randint(1, 10)
    operator = choice(['+', '-', '*'])

    expression = str(operand1) + ' ' + operator + ' ' + str(operand2)
    correct_answer = eval(expression)

    return expression, str(correct_answer)
