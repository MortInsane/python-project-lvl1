from random import randint
from math import gcd


GAME_RULE = 'Find the greatest common divisor of given numbers.'
START_RANGE = 1
STOP_RANGE = 100


def generate_round():
    number1 = randint(START_RANGE, STOP_RANGE)
    number2 = randint(START_RANGE, STOP_RANGE)

    answer = str(gcd(number1, number2))
    question = f'{number1} {number2}'

    return answer, question
