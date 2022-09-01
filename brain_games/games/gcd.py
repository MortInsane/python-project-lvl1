from random import randint
from math import gcd


GAME_CONDITION = 'Find the greatest common divisor of given numbers.'
START = 1
STOP = 100


def gcd_logic():

    NUMBER1 = randint(START, STOP)
    NUMBER2 = randint(START, STOP)

    success_answer = str(gcd(NUMBER1, NUMBER2))
    question_print = f'{NUMBER1} {NUMBER2}'

    return success_answer, question_print
