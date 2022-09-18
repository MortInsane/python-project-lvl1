from random import randint


GAME_RULE = 'What number is missing in the progression?'
MIN_STEP = 2
MAX_STEP = 10
START_RANGE = 1
STOP_RANGE = 100
LENGHT_PROGRESSION = 10


def generate_round():
    step_progression = randint(MIN_STEP, MAX_STEP)
    start_progression = randint(START_RANGE, STOP_RANGE)
    end_progression = start_progression + LENGHT_PROGRESSION * step_progression

    question = ''
    replaced_index = randint(START_RANGE - 1, LENGHT_PROGRESSION - 1)
    answer = 0

    for index, num in enumerate(range(start_progression,
                                      end_progression,
                                      step_progression)):
        if index == replaced_index:
            question += '.. '
            answer = num
        else:
            question += f'{str(num)} '

    question = question.strip()
    answer = str(answer)

    return answer, question
