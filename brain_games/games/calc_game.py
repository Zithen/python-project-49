from random import randint


RULES = 'What is the result of the expression?'


def question():
    operand1 = randint(1, 1000)
    operand2 = randint(1, 1000)
    operators = ['+', '-', '*']
    operator = operators[randint(0, 2)]
    expression = operand1 + ' ' + operator + ' ' + operand2
    return expression


def game(question):
    correct_answer = eval(question)

    return str(correct_answer)
