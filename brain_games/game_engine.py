import prompt


ROUNDS_COUNT = 3


def launch_game(game):
    success_answers_count = 0

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_RULE)

    while True:
        answer, question = game.generate_round()

        if success_answers_count == ROUNDS_COUNT:
            print(f'Congratulations, {name}!')
            return

        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == answer:
            print('Correct!')
            success_answers_count += 1
        else:
            print(f'\'{user_answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{answer}\'\n'
                  f'Let\'s try again, {name}!')
            return
