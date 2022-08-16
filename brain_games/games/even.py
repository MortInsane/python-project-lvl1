from brain_games.game_engine import welcome_user, game_checker
from random import randint


GAME_CONDITION = 'Answer "yes" if the number is even, otherwise answer "no".'


def even_logic():
    count_success_answer = 0
    name = welcome_user()

    while True:
        if count_success_answer == 3:
            print(f'Congratulations, {name}!')
            return

        number = randint(1, 100)
        yes_answer, no_answer = 'yes', 'no'

        if number % 2 == 0:
            success_answer = yes_answer
        else:
            success_answer = no_answer

        question_print = str(number)
        attempt = game_checker(question=question_print,
                               success_answer=success_answer)

        if attempt == 'correct':
            print('Correct!')
            count_success_answer += 1
        else:
            print(f"'{attempt}' is wrong answer ;(. "
                  f"Correct answer was '{success_answer}'\n"
                  f"Let's try again, {name}!")
            return
