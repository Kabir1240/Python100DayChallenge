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
    
    wins_against = {
        0: 2,  # Rock beats Scissors
        1: 0,  # Paper beats Rock
        2: 1   # Scissors beats Paper
    }
    
    while True:
        try:
            # Pick choices for player and cpu
            # 0 = rock, 1 = paper, 2 = scissors 3 = quit
            player_choice = int(input("What do you choose? Type 1 for rock, 2 for paper and 3 for scissors and 4 to exit.\n")) - 1
            
            if player_choice == 3:
                print("Thanks for playing!")
                break
            
            cpu_choice = random.randint(0, 2)
        
            # Display both choices
            print(f"You Chose: {rps_art[player_choice]}")
            print(f"The CPU chose: {rps_art[cpu_choice]}")
            
            # logic
            if player_choice == cpu_choice:
                print("It's a draw!")
            elif wins_against[player_choice] == cpu_choice:
                print("You win!")
            else:
                print("You lose!")
                
        except ValueError:
            print("Invalid Input, please choose type 1, 2 or 3")
            continue

rps()
