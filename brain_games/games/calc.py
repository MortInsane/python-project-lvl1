from brain_games.game_engine import welcome_user, game_checker
from random import randint, choice


GAME_CONDITION = "What is the result of the expression?"


def calc_logic():
    count_success_answer = 0
    name = welcome_user(GAME_CONDITION)
    operators = ['+', '-', '*']

    while True:
        if count_success_answer == 3:
            print(f'Congratulations, {name}!')
            return

        operator = choice(operators)
        number1 = randint(1, 100)
        number2 = randint(1, 100)

        success_answer = 0
        if operator == '-':
            success_answer = number1 - number2
        elif operator == '+':
            success_answer = number1 + number2
        else:
            success_answer = number1 * number2

        success_answer = str(success_answer)
        question_print = f"{number1} {operator} {number2}"
        attempt = game_checker(question=question_print,
                               success_answer=success_answer)

        if attempt == 'correct':
            print('Correct!')
            count_success_answer += 1
        else:
            print(f"'{attempt}' is wrong answer ;(. "
                  f"Correct answer was '{success_answer}'\n"
                  f"Let's try again, {name}!")
            return
