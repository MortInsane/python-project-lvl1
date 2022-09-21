from random import randint


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
START_RANGE = 1
STOP_RANGE = 100


def is_even(num):
    answer = ''

    if num % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'

    return answer


def generate_round():
    number = randint(START_RANGE, STOP_RANGE)

    answer = is_even(number)
    question = str(number)

    return answer, question
