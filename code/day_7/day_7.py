from random_word import RandomWords
from ascii_art import stages, title
# from word_list import word_list
# import random

def hangman():
    #Step 1
    # ===== Alternative method to obtain random word
    # list_of_words = word_list
    # chosen_word = random.choice(list_of_words)

    # Show introduction. Create display. Set up chosen word
    print("Welcome to...")
    print(title)
    chosen_word = RandomWords().get_random_word()
    len_word = len(chosen_word)
    display = []
    for _ in chosen_word:
        display.append('_')
    print(display)
    print(stages[6])

    letters_guessed = []
    game_over = False
    lives = 6
    correct_guesses = 0
    while not game_over:
        # get guess from user
        guess = input("Guess a letter: ").lower()
        if guess in letters_guessed:
            print(f"You already guessed {guess}, try something else!")
        else:
            letters_guessed.append(guess)
            #check if guess is in the chosen_word or not
            match = False
            # you could do it with 'if guess in chosen_word' as well
            for letter_pos in range(len_word):
                letter = chosen_word[letter_pos]
                if letter == guess:
                    display[letter_pos] = guess
                    correct_guesses += 1
                    match = True

            print(display)
            print(stages[lives])
            # if the user guessed wrong
            if not match:
                print(f"You guessed {guess}. That's not in the word. You lose a life :(")
                lives -= 1
                # game over conditions
                if lives == 0:
                    print("Game Over")
                    game_over = True
            else:
                if correct_guesses == len_word:
                    print("You Won!")
                    game_over = True

hangman()