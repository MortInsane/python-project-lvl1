from random import randint


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START_RANGE = 1
STOP_RANGE = 100


def is_prime(number):
    if number < 2:
        return False

    divisor = 2
    while number % divisor != 0:
        divisor += 1
    return number == divisor


def generate_round():
    number = randint(START_RANGE, STOP_RANGE)

    if is_prime(number):
        answer = 'yes'
    else:
        answer = 'no'

    question = str(number)

    return answer, question
