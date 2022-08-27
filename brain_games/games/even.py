from brain_games.game_engine import run_game
from random import randint


GAME_CONDITION = 'Answer "yes" if the number is even, otherwise answer "no".'


def even_logic():
    NUMBER = randint(1, 100)
    yes_answer, no_answer = 'yes', 'no'

    if NUMBER % 2 == 0:
        success_answer = yes_answer
    else:
        success_answer = no_answer

    question_print = str(NUMBER)

    return success_answer, question_print


def run_game_even():
    run_game(game_condition=GAME_CONDITION, game=even_logic)
