from random import randint, choice


GAME_RULE = 'What is the result of the expression?'
START_RANGE = 1
STOP_RANGE = 100
OPERATORS = ['+', '-', '*']


def get_expression(num1, num2, operator):
    answer = 0

    if operator == '-':
        answer = num1 - num2
    elif operator == '+':
        answer = num1 + num2
    elif operator == '*':
        answer = num1 * num2

    return str(answer)


def generate_round():
    number1 = randint(START_RANGE, STOP_RANGE)
    number2 = randint(START_RANGE, STOP_RANGE)
    operator = choice(OPERATORS)

    answer = get_expression(number1, number2, operator)
    question = f'{number1} {operator} {number2}'

    return answer, question
