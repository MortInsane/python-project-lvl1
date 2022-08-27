from brain_games.game_engine import run_game
from random import randint, choice


GAME_CONDITION = "What is the result of the expression?"


def calc_logic():
    NUMBER1 = randint(1, 100)
    NUMBER2 = randint(1, 100)

    OPERATORS = ['+', '-', '*']
    operator = choice(OPERATORS)

    success_answer = 0
    if operator == '-':
        success_answer = NUMBER1 - NUMBER2
    elif operator == '+':
        success_answer = NUMBER1 + NUMBER2
    else:
        success_answer = NUMBER1 * NUMBER2

    success_answer = str(success_answer)
    question_print = f"{NUMBER1} {operator} {NUMBER2}"

    return success_answer, question_print


def run_game_calc():
    run_game(game_condition=GAME_CONDITION, game=calc_logic)
