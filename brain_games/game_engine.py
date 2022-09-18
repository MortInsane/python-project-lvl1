import prompt


ROUNDS_COUNT = 3


def launch_game(game):
    success_answers_count = 0

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_RULE)

    round = 0
    while round < ROUNDS_COUNT:
        answer, question = game.generate_round()

        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == answer:
            print('Correct!')
            success_answers_count += 1
            round += 1
        else:
            print(f'\'{user_answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{answer}\'\n'
                  f'Let\'s try again, {name}!')
            return

    print(f'Congratulations, {name}!')
