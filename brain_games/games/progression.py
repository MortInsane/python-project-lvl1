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

    question = []

    for num in range(start_progression, end_progression, step_progression):
        question.append(str(num))

    replaced_index = randint(0, LENGHT_PROGRESSION - 1)
    answer = str(question[replaced_index])
    question[replaced_index] = '..'

    question = ' '.join(question)

    return answer, question
