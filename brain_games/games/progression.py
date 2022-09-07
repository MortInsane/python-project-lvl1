from random import randint, choice


GAME_RULE = 'What number is missing in the progression?'
OFFSETS = [2, 3, 4, 5]
START_RANGE = 1
STOP_RANGE = 100
NUMBER = 10


def print_progression():
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
    replaced_num = str(replaced_num)

    return progression, replaced_num


def game_logic():
    question, answer = print_progression()

    return answer, question, GAME_RULE
