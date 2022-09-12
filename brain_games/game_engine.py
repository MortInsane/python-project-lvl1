import prompt


ROUND_COUNT = 3


def launch_engine(game):
    count_success_answer = 0

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_RULE)

    while True:
        answer, question = game.launch_game()

        if count_success_answer == ROUND_COUNT:
            print(f'Congratulations, {name}!')
            return

        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == answer:
            print('Correct!')
            count_success_answer += 1
        else:
            print(f'\'{user_answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{answer}\'\n'
                  f'Let\'s try again, {name}!')
            return
