from random import randint


GAME_RULE = 'What number is missing in the progression?'
MIN_STEP = 2
MAX_STEP = 10
START_RANGE = 1
STOP_RANGE = 100
LENGHT_PROGRESSION = 10


def generate_progression(start, end, step, lenght):
    progression = []

    for num in range(start, end, step):
        progression.append(str(num))

    replaced_index = randint(0, lenght - 1)
    answer = str(progression[replaced_index])
    progression[replaced_index] = '..'
    progression = ' '.join(progression)

    return answer, progression


def generate_round():
    start_progression = randint(START_RANGE, STOP_RANGE)
    step_progression = randint(MIN_STEP, MAX_STEP)
    end_progression = start_progression + LENGHT_PROGRESSION * step_progression

    answer, question = generate_progression(start_progression,
                                            end_progression,
                                            step_progression,
                                            LENGHT_PROGRESSION)

    return answer, question
