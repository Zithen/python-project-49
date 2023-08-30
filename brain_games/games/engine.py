from prompt import string


def engine(game):
    questions_to_ask = 3
    print('Welcome to the Brain Games!')

    user_name = string('May I have your name? ')
    print(f'Hello, {user_name}')

    print(game.RULES)

    for _ in range(questions_to_ask):
        question = game.question()
        correct_answer = game.game(question)
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
