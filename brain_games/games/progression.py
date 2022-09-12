from random import randint, choice


GAME_RULE = 'What number is missing in the progression?'
OFFSETS = [2, 3, 4, 5]
START_RANGE = 1
STOP_RANGE = 100
LENGHT_PROGRESSION = 10


def launch_game():
    offset = choice(OFFSETS)
    start = randint(START_RANGE, STOP_RANGE)
    end = start + (LENGHT_PROGRESSION * offset)

    question = ''
    replaced_index = choice(range(LENGHT_PROGRESSION))
    answer = 0

    for index, num in enumerate(range(start, end, offset)):
        if index == replaced_index:
            question += '.. '
            answer = num
        else:
            question += f'{str(num)} '

    question = question.strip()
    answer = str(answer)

    return answer, question
