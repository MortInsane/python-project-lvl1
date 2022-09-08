from random import randint, choice


GAME_RULE = 'What is the result of the expression?'
START = 1
STOP = 100
OPERATORS = ['+', '-', '*']


def game_logic():
    number1 = randint(START, STOP)
    number2 = randint(START, STOP)

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
