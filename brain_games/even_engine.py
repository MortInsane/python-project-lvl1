import prompt
from brain_games.cli import welcome_user
from random import randint


def even_logic():
    count_success_answer = 0

    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    while True:
        if count_success_answer == 3:
            print(f'Congratulations, {name}!')
            return

        number = randint(1, 100)
        yes_answer, no_answer = 'yes', 'no'

        if number % 2 == 0:
            success_answer = yes_answer
        else:
            success_answer = no_answer

        print(f"Question: {number}")
        answer = prompt.string('Your answer: ')

        if answer == success_answer:
            count_success_answer += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f"Correct answer was '{success_answer}'\n"
                  f"Let's try again, {name}")
            return
