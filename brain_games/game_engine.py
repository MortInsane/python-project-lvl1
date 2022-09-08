import prompt


def run_game(game):
    count_success_answer = 0

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_RULE)

    while True:
        answer, question = game.game_logic()

        if count_success_answer == 3:
            print(f'Congratulations, {name}!')
            return

        print(f'Question: {question}')
        attempt = prompt.string('Your answer: ')

        if attempt == answer:
            print('Correct!')
            count_success_answer += 1
        else:
            print(f'\'{attempt}\' is wrong answer ;(. '
                  f'Correct answer was \'{answer}\'\n'
                  f'Let\'s try again, {name}!')
            return
