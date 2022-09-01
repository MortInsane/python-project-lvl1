from random import randint, choice


GAME_CONDITION = 'What is the result of the expression?'
START = 1
STOP = 100
OPERATORS = ['+', '-', '*']


def calc_logic():
    NUMBER1 = randint(START, STOP)
    NUMBER2 = randint(START, STOP)

    operator = choice(OPERATORS)

    success_answer = 0
    if operator == '-':
        success_answer = NUMBER1 - NUMBER2
    elif operator == '+':
        success_answer = NUMBER1 + NUMBER2
    else:
        success_answer = NUMBER1 * NUMBER2

    success_answer = str(success_answer)
    question_print = f'{NUMBER1} {operator} {NUMBER2}'

    return success_answer, question_print
