from random import randint, choice


GAME_RULE = 'What is the result of the expression?'
START_RANGE = 1
STOP_RANGE = 100
OPERATORS = ['+', '-', '*']


def generate_round():
    number1 = randint(START_RANGE, STOP_RANGE)
    number2 = randint(START_RANGE, STOP_RANGE)

    operator = choice(OPERATORS)

    answer = 0
    if operator == '-':
        answer = number1 - number2
    elif operator == '+':
        answer = number1 + number2
    elif operator == '*':
        answer = number1 * number2

    answer = str(answer)
    question = f'{number1} {operator} {number2}'

    return answer, question
