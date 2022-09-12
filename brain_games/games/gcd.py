from random import randint
from math import gcd


GAME_RULE = 'Find the greatest common divisor of given numbers.'
START = 1
STOP = 100


def launch_game():

    number1 = randint(START, STOP)
    number2 = randint(START, STOP)

    answer = str(gcd(number1, number2))
    question = f'{number1} {number2}'

    return answer, question
