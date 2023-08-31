from prompt import string


QUESTIONS_TO_ASK = 3


def engine(game):
    print('Welcome to the Brain Games!')

    user_name = string('May I have your name? ')
    print(f'Hello, {user_name}')

    print(game.RULES)

    for _ in range(QUESTIONS_TO_ASK):
        question, correct_answer = game.game_logic()

        print(f'Question: {question}')
        user_answer = string('Your answer: ')

        if correct_answer != user_answer:
            print(f'"{user_answer}" is wrong answer ;(.', end=' ')
            print(f'Correct answer was "{correct_answer}".')
            print(f"Let's try again, {user_name}!")
            return 1
        else:
            print('Correct!')

    print(f'Congratulations, {user_name}!')
