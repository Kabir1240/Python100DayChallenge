def love_calculator():
    print("The Love Calculator is calculating your score...")
    name1 = input("input the first name\n")  # What is your name?
    name2 = input("input the second name\n")  # What is their name?
    # 🚨 Don't change the code above 👆
    # Write your code below this line 👇
    score_true = 0
    score_love = 0
    name_combined = (name1 + name2).lower()

    # calculate score for True
    t_occur = name_combined.count('t')
    r_occur = name_combined.count('r')
    u_occur = name_combined.count('u')
    e_occur = name_combined.count('e')

    score_true += t_occur + r_occur + u_occur + e_occur
    score_true = str(score_true)

    # calculate score for Love
    l_occur = name_combined.count('l')
    o_occur = name_combined.count('o')
    v_occur = name_combined.count('v')

    score_love += l_occur + o_occur + v_occur + e_occur
    score_love = str(score_love)

    # putting it together
    final_score = int(score_true + score_love)

    if final_score < 10 or final_score > 90:
        print(f"Your score is {final_score}, you go together like coke and mentos.")
    elif 40 <= final_score <= 50:
        print(f"Your score is {final_score}, you are alright together.")
    else:
        print(f"Your score is {final_score}.")

def treasure_island_game():
    print("Welcome to the treasure island! Your mission is to find the treasure.\n")
    want_shake = input("\n The pirate greets you, do you want to shake his hand?\n")
    if want_shake.lower() == "yes" or want_shake.lower() == 'y':
        print('''
                         _____
                      .-" .-. "-.
                    _/ '=(0.0)=' \_
                  /`   .='|m|'=.   `\
                  \________________ /
              .--.__///`'-,__~\\\\~`
             / /6|__\// a (__)-\\\\
             \ \/--`((   ._\   ,)))
             /  \\  ))\  -==-  (O)(
            /    )\((((\   .  /)))))
           /  _.' /  __(`~~~~`)__
          //"\\,-'-"`   `~~~~\\~~`"-.
         //  /`"              `      `\
        //

                   ''')
        print("The pirate killed you")
        game_over()
    elif want_shake.lower() == "no" or want_shake.lower() == 'n':
        print("The pirate tries to attack you, but you run away")

    want_swim = input("\nYou managed to find a river and see a 'X' on the other side, do you wan to swim?\n")
    if want_swim.lower() == "yes" or want_swim.lower() == 'y':
        print("You were eaten by a crocodile...\n")
        print('''
                            .-._   _ _ _ _ _ _ _ _
         .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
         '.___ '    .   .--_'-' '-' '-' _'-' '._
          V: V 'vv-'   '_   '.       .'  _..' '.'.
            '=.____.=_.--'   :_.__.__:_   '.   : :
                    (((____.-'        '-.  /   : :
          snd                         (((-'\ .' /
                                    _____..'  .'
                                   '-._____.-'
        ''')
        game_over()
    elif want_swim.lower() == "no" or want_swim.lower() == 'n':
        print("The pirate tries to attack you, but you run away")

    door = input("\nYou ignore the river and keep walking. After a while, you encounter 3 doors. Which one do you want to"
          "choose? Left, right or middle?\n")
    if door.lower() == "left" or door.lower() == 'l' or door.lower() == '1':
        print("You run into the first door and find yourself falling to your death...")
        game_over()
    elif door.lower() == "right" or door.lower() == "r" or door.lower() == '3':
        print("You stumble into the second door. As you enter, you see the 'X' mark under your feet and proceed to dig"
              ". Eventually you hit a hard surface and find it...")
        print('''\n
        *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
        ''')
        print("\nCONGRATS! You won the game!")

    elif door.lower() == "middle" or door.lower() == 'm' or door.lower() == '2':
        print('''
             /~~~\   /~~\
            (     | |    )
            |     | |    |
             \   (  |   /'/~\
         /~~\ \   )  \/' /'  |
         |   \ `\/      /    |
          \   )   /~\  |    /'
           `~~  /'   `\ \__/
       Ts97    |       ~\
             /~          \
             `\  __     /'
               `~  `~~~'
        ''')

        print("\nYou see a large footprint, followed by an extremely loud grumble. You turn to walk away, but the"
              "door is gone.")
        game_over()
def game_over():
    print("GAME OVER")
    print("You died, damn you suck")
    quit()

treasure_island_game()