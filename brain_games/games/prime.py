from brain_games.game_engine import run_game
from random import randint


GAME_CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(a):
    d = 2
    while a % d != 0:
        d += 1
    return a == d


def prime_logic():
    NUMBER = randint(2, 100)
    yes_answer, no_answer = 'yes', 'no'

    if is_prime(NUMBER):
        success_answer = yes_answer
    else:
        success_answer = no_answer

    question_print = str(NUMBER)

    return success_answer, question_print


def run_game_prime():
    run_game(game_condition=GAME_CONDITION, game=prime_logic)
