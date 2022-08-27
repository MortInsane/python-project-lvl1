from brain_games.game_engine import run_game
from random import randint, choice


GAME_CONDITION = 'What number is missing in the progression?'


def draw_progression():
    offset = choice([2, 3, 4, 5])
    start = randint(1, 100)
    end = start + (10 * offset)

    progression = ''
    replaced_index = choice(range(10))
    replaced_num = 0
    for index, num in enumerate(range(start, end, offset)):
        if index == replaced_index:
            progression += ".. "
            replaced_num = num
        else:
            progression += f"{str(num)} "
    progression = progression.strip()

    return progression, replaced_num


def progression_logic():
    question, success_answer = draw_progression()
    success_answer = str(success_answer)

    question_print = question

    return success_answer, question_print


def run_game_progression():
    run_game(game_condition=GAME_CONDITION, game=progression_logic)
