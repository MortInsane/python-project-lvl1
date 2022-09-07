from random import randint


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'
START = 1
STOP = 100


def game_logic():
    number = randint(START, STOP)

    if number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'

    question = str(number)

    return answer, question, GAME_RULE
