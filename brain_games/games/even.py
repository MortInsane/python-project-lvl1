from random import randint


GAME_CONDITION = 'Answer "yes" if the number is even, otherwise answer "no".'
START = 1
STOP = 100


def even_logic():
    NUMBER = randint(START, STOP)

    if NUMBER % 2 == 0:
        success_answer = 'yes'
    else:
        success_answer = 'no'

    question_print = str(NUMBER)

    return success_answer, question_print
