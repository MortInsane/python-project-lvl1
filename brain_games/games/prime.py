from brain_games.game_engine import welcome_user, game_checker
from random import randint


GAME_CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(a):
    d = 2
    while a % d != 0:
        d += 1
    return a == d


def prime_logic():
    count_success_answer = 0
    name = welcome_user(GAME_CONDITION)

    while True:
        if count_success_answer == 3:
            print(f'Congratulations, {name}!')
            return

        number = randint(2, 100)
        yes_answer, no_answer = 'yes', 'no'

        if is_prime(number):
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
