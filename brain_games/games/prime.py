from random import randint


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START = 1
STOP = 100


def is_prime(a):
    if a < 2:
        return False

    d = 2
    while a % d != 0:
        d += 1
    return a == d


def game_logic():
    number = randint(START, STOP)

    if is_prime(number):
        answer = 'yes'
    else:
        answer = 'no'

    question = str(number)

    return answer, question, GAME_RULE
