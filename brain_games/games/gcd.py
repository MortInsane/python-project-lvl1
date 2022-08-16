from brain_games.game_engine import welcome_user, game_checker
from random import randint


GAME_CONDITION = 'Find the greatest common divisor of given numbers.'


def get_fast_gcd(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a


def gcd_logic():
    count_success_answer = 0
    name = welcome_user(GAME_CONDITION)

    while True:
        if count_success_answer == 3:
            print(f'Congratulations, {name}!')
            return

        number1 = randint(1, 100)
        number2 = randint(1, 100)

        success_answer = str(get_fast_gcd(number1, number2))
        question_print = f'{number1} {number2}'

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
