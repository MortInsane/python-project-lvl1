from random import randint


GAME_RULE = 'What number is missing in the progression?'
MIN_STEP = 2
MAX_STEP = 10
START_RANGE = 1
STOP_RANGE = 100
LENGHT = 10


def generate_progression(start, end, step, replaced_index):
    progression = []

    for num in range(start, end, step):
        progression.append(str(num))

    answer = str(progression[replaced_index])
    progression[replaced_index] = '..'
    progression = ' '.join(progression)

    return answer, progression


def generate_round():
    start_progression = randint(START_RANGE, STOP_RANGE)
    step_progression = randint(MIN_STEP, MAX_STEP)
    end_progression = start_progression + LENGHT * step_progression
    replaced_index = randint(0, LENGHT - 1)

    answer, question = generate_progression(start_progression,
                                            end_progression,
                                            step_progression,
                                            replaced_index)

    return answer, question
