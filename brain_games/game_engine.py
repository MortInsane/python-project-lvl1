import prompt


def welcome_user(game_condition):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_condition)
    return name


def game_checker(question, success_answer):
    print(f"Question: {question}")
    user_answer = prompt.string('Your answer: ')

    if user_answer == success_answer:
        return 'correct'
    else:
        return user_answer
