from turtle import Turtle
PADDLE_SIZE = 4
PADDLE_SPEED = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.setheading(90)
        self.speed("fastest")
        self.shapesize(stretch_len=PADDLE_SIZE)
        self.goto(position)

    def move_up(self):
        if self.ycor() >= 350:
            return False
        else:
            new_y = self.ycor() + PADDLE_SPEED
            self.goto(self.xcor(), new_y)
            return True

    def move_down(self):
        if self.ycor() <= -350:
            return False
        else:
            new_y = self.ycor() - PADDLE_SPEED
            self.goto(self.xcor(), new_y)
            return True