from brain_games.game_engine import welcome_user, game_checker
from random import randint, choice


GAME_CONDITION = 'What number is missing in the progression?'


def draw_progression():
    offset = choice([2, 3, 4, 5])
    start = randint(1, 100)
    end = start + (10 * offset)

    progression = ''
    replaced_index = choice(range(10))
    replaced_num = 0
    for index, num in enumerate(range(start, end, offset)):
        if index == replaced_index:
            progression += ".. "
            replaced_num = num
        else:
            progression += f"{str(num)} "
    progression = progression.strip()

    return progression, replaced_num


def progression_logic():
    count_success_answer = 0
    name = welcome_user(GAME_CONDITION)

    while True:
        if count_success_answer == 3:
            print(f'Congratulations, {name}!')
            return

        question, success_answer = draw_progression()
        success_answer = str(success_answer)

        question_print = question
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
