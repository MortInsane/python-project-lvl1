from random import randint, choice


GAME_CONDITION = 'What number is missing in the progression?'
OFFSETS = [2, 3, 4, 5]
START_RANGE = 1
STOP_RANGE = 100
NUMBER = 10


def draw_progression():
    offset = choice(OFFSETS)
    start = randint(START_RANGE, STOP_RANGE)
    end = start + (NUMBER * offset)

    progression = ''
    replaced_index = choice(range(NUMBER))
    replaced_num = 0
    for index, num in enumerate(range(start, end, offset)):
        if index == replaced_index:
            progression += '.. '
            replaced_num = num
        else:
            progression += f'{str(num)} '
    progression = progression.strip()

    return progression, replaced_num


def progression_logic():
    question, success_answer = draw_progression()
    success_answer = str(success_answer)

    question_print = question

    return success_answer, question_print
