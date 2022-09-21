from random import randint


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
START_RANGE = 1
STOP_RANGE = 100


def is_even(num):
    if num % 2 == 0:
        return True

    return False


def generate_round():
    number = randint(START_RANGE, STOP_RANGE)

    if is_even(number):
        answer = 'yes'
    else:
        answer = 'no'

    question = str(number)

    return answer, question
