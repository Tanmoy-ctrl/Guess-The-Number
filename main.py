import random
easy_level_attempts=10
hard_level_attempts=5
def set_difficulty(level_chosen):
    if level_chosen=='easy':
        return easy_level_attempts
    else:
        return hard_level_attempts
def check_answer(guessed_number,answer,attempts):
    if guessed_number<answer:
        print("Your guess is too low.")
        return attempts-1
    elif guessed_number>answer:
        print("Your guess is too high.")
        return attempts-1
    else:
        print(f"Your guess is right...The answer was {answer}.")
def game():
    print("Let me think of a number between 1 to 50:")
    answer=random.randint(1,50)
    level=input("Choose level of difficulty...Type 'easy' or 'hard':")
    attempts=set_difficulty(level)
    guessed_number=0
    while guessed_number!=answer:
        print(f"You have {attempts} to guess the number.")
        guessed_number=int(input("Guess a number:"))
        attempts=check_answer(guessed_number,answer,attempts)
        if attempts==0:
            print("You are out of guesses...You lose!")
            return
        elif guessed_number!=answer:
            print("Guess again.")
game()
