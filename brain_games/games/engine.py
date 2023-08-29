from prompt import string


def engine(game):
    questions_to_ask = 3
    print('Welcome to the Brain Games!')

    user_name = string('May I have your name? ')
    print(f'Hello, {user_name}')

    for _ in range(questions_to_ask):
        correct_answer = game.get('correct_answer')
        user_answer = game.get('user_answer')
