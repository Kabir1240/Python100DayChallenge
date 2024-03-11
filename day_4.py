import random
"""
All ascii art by wynand1004 on github
link: https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe
"""

def rps():
    #store art
    rock_art = """
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """

    paper_art = """
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """

    scissors_art = """
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """

    rps_art = [rock_art, paper_art, scissors_art]

    # 0 = rock, 1 = paper, 2 = scissors
    cpu_choice = random.randint(0, 2)
    player_choice = int(input("What do you choose? Type 1 for rock, 2 for paper and 3 for scissors.\n")) - 1

    if player_choice >= 3 or player_choice < 0:
        print("Invalid Input, please choose type 1, 2 or 3")
    else:
        # Display both choices
        print("You Chose: ")
        print(rps_art[player_choice])
        print("The CPU chose: ")
        print(rps_art[cpu_choice])

        # logic
        if player_choice == 2 and cpu_choice == 0:
            print("You Lose...")
        elif cpu_choice == 2 and player_choice == 0:
            print("Congrats! You Won!")
        elif cpu_choice > player_choice:
            print("You Lose...")
        elif player_choice > cpu_choice:
            print("Congrats! You Won!")
        elif player_choice == cpu_choice:
            print("It Was a Draw :(")


rps()