import prompt


def welcome_user(game_condition):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_condition)
    return name


def game_checker(question, success_answer):
    print(f'Question: {question}')
    user_answer = prompt.string('Your answer: ')

    if user_answer == success_answer:
        return 'correct'
    else:
        return user_answer


def run_game(game_condition, game):
    count_success_answer = 0
    name = welcome_user(game_condition)

    while True:
        success_answer, question_print = game()

        if count_success_answer == 3:
            print(f'Congratulations, {name}!')
            return

        attempt = game_checker(question=question_print,
                               success_answer=success_answer)

        if attempt == 'correct':
            print('Correct!')
            count_success_answer += 1
        else:
            print(f'\'{attempt}\' is wrong answer ;(. '
                  f'Correct answer was \'{success_answer}\'\n'
                  f'Let\'s try again, {name}!')
            return
