from prompt import string


def engine(game):
    questions_to_ask = 3
    print('Welcome to the Brain Games!')

    user_name = string('May I have your name? ')
    print(f'Hello, {user_name}')

    print(game.get('rules'))

    for _ in range(questions_to_ask):
        question = game.get('question')
        correct_answer = game.get('correct_answer')
        user_answer = game.get('user_answer')

        print(f'Question: {question}')

        if correct_answer != user_answer:
            print(f'{user_answer} is wrong answer ;(.', end=' ')
            print(f'Correct answer was {correct_answer}.')
            print(f"Let's try again, {user_name}!")
            return 1
        else:
            print('Correct!')

    print(f'Congratulations, {user_name}!')
