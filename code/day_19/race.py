from turtle import Turtle, Screen
import random


def race() -> None:
    """
    Game that uses Turtle graphics. Starts a race between 6 turtles with 6 different colors. The user can bet on who
    they think will win. The result is announces at the end.
    :return: None
    """

    # initial colors of turtles
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    # init turtles and screen
    turtles = create_turtles(colors)
    screen = Screen()
    screen.setup(width=500, height=400)

    # game logic starts here.
    is_race_on = False
    # allows user to make bet. Keeps asking until user inputs an acceptable response.
    user_bet = screen.textinput(title="Make A Bet", prompt="Which turtle do you think will win the race?")
    while user_bet.lower() not in colors:
        user_bet = screen.textinput(title="Invalid", prompt="Pick from red, green, blue, yellow, purple or orange")

    # start the race
    if user_bet:
        is_race_on = True

    while is_race_on:
        # each turtle moves randomly from a distance of 1 to 10
        for turtle in turtles:
            random_distance = random.randint(1, 10)
            turtle.forward(random_distance)

            # if a turtle reaches the end, the game is exited and winner is announced
            if turtle.xcor() >= 200:
                is_race_on = False
                winner = turtle.pencolor()
                if winner == user_bet:
                    print(f"You've won! The {winner} turtle is the winner!")
                else:
                    print(f"You've lost! The {winner} turtle is the winner!")
                break

    screen.exitonclick()


def create_turtles(colors) -> list:
    """
    creates turtle for the race game, based on colors in the list given
    :param colors: list of colors
    :return: an array of Turtle objects
    """
    # return value
    turtles = []

    # coordinates of turtles
    x = -220
    y = 130
    for color in colors:
        new_turtle = Turtle("turtle")
        new_turtle.color(color)
        new_turtle.penup()
        new_turtle.goto(x=x, y=y)
        turtles.append(new_turtle)
        y -= 50

    # return array
    return turtles


race()
