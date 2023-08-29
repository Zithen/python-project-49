from prompt import string


def engine(game_params_dict):
    questions_to_ask = 3
    print('Welcome to the Brain Games!')

    user_name = string('May I have your name? ')
    print(f'Hello, {user_name}')

    print(game_params_dict.get('rules'))

    for _ in range(questions_to_ask):
        question = game_params_dict.get('question')
        correct_answer = game_params_dict.get('correct_answer')

        print(f'Question: {question}')
        user_answer = string('Your answer: ')

        if correct_answer != user_answer:
            print(f'{user_answer} is wrong answer ;(.', end=' ')
            print(f'Correct answer was {correct_answer}.')
            print(f"Let's try again, {user_name}!")
            return 1
        else:
            print('Correct!')

    print(f'Congratulations, {user_name}!')
