from brain_games.game_engine import run_game
from random import randint


GAME_CONDITION = 'Find the greatest common divisor of given numbers.'


def get_fast_gcd(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a


def gcd_logic():

    NUMBER1 = randint(1, 100)
    NUMBER2 = randint(1, 100)

    success_answer = str(get_fast_gcd(NUMBER1, NUMBER2))
    question_print = f'{NUMBER1} {NUMBER2}'

    return success_answer, question_print


def run_game_gcd():
    run_game(game_condition=GAME_CONDITION, game=gcd_logic)
