from turtle import Turtle
import random
INITIAL_HEADINGS = [(20, 20), (-20, -20)]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        current_heading = random.choice(INITIAL_HEADINGS)
        self.x_move = current_heading[0]
        self.y_move = current_heading[1]
        self.shape("circle")
        self.color("white")
        self.move_speed = 0.0005
        self.penup()

    def speed_up(self):
        self.move_speed /= 100

    def slow_down(self):
        self.move_speed = 0.0005

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def contact_floor_ceil(self):
        self.y_move *= -1

    def contact_paddle(self):
        self.x_move *= -1
        self.speed_up()

    def to_centre(self):
        self.slow_down()
        self.hideturtle()
        self.goto(0, 0)
        self.showturtle()

        self.x_move *= -1
