import random


EASY_LEVEL_ATTEMPTS = 50
HARD_LEVEL_ATTEMPTS = 10

def number_guessing_game(a, b):
    random_number = random.randint(a, b)
    print(random_number)
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {a} and {b}")
    difficulty = input("Choose difficulty 'Easy' or 'Hard': \n")

    while not (difficulty.lower() == "easy" or difficulty.lower() == "hard"):
        difficulty = input("Please type 'Easy' or 'Hard': \n")

    tries = 0
    if difficulty.lower() == 'hard':
        tries = HARD_LEVEL_ATTEMPTS
    elif difficulty.lower() == 'easy':
        tries = EASY_LEVEL_ATTEMPTS

    while tries != 0:
        guess = int(input("Make a guess: "))
        if guess > random_number:
            print("Too High.")
            tries -= 1
        elif guess < random_number:
            print("Too Low.")
            tries -= 1
        elif guess == random_number:
            print("You Got It!!")
            break

        if tries > 0:
            print("Guess again.")
            print(f"You have {tries} attempts remaining to guess the number")
            continue
        if tries == 0:
            print("Sorry, you lost. Better luck next time")


number_guessing_game(1, 100)