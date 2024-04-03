from turtle import Turtle, Screen
import random


def race():
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    turtles = create_turtles(colors)
    screen = Screen()
    screen.setup(width=500, height=400)

    is_race_on = False
    user_bet = screen.textinput(title="Make A Bet", prompt="Which turtle do you think will win the race?")
    while user_bet.lower() not in colors:
        user_bet = screen.textinput(title="Invalid", prompt="Pick from red, green, blue, yellow, purple or orange")

    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle in turtles:
            random_distance = random.randint(1, 10)
            turtle.forward(random_distance)

            if turtle.xcor() >= 200:
                is_race_on = False
                winner = turtle.pencolor()
                if winner == user_bet:
                    print(f"You've won! The {winner} turtle is the winner!")
                else:
                    print(f"You've lost! The {winner} turtle is the winner!")
                break

    screen.exitonclick()


def create_turtles(colors):
    turtles = []

    x = -220
    y = 130
    for color in colors:
        new_turtle = Turtle("turtle")
        new_turtle.color(color)
        new_turtle.penup()
        new_turtle.goto(x=x, y=y)
        turtles.append(new_turtle)
        y -= 50

    return turtles


race()
