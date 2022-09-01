from random import randint


GAME_CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START = 1
STOP = 100


def is_prime(a):
    if a < 2:
        return False

    d = 2
    while a % d != 0:
        d += 1
    return a == d


def prime_logic():
    NUMBER = randint(START, STOP)

    if is_prime(NUMBER):
        success_answer = 'yes'
    else:
        success_answer = 'no'

    question_print = str(NUMBER)

    return success_answer, question_print
