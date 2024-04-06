from turtle import Turtle
PADDLE_SIZE = 4
PADDLE_SPEED = 20


class Paddle(Turtle):
    """
    Paddle class for Pong game.
    """
    def __init__(self, position):
        """
        Initializes the paddle, sends it to the appropriate position.
        :param position: Position to send the paddle.
        """
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.setheading(90)
        self.speed("fastest")
        self.shapesize(stretch_len=PADDLE_SIZE)
        self.goto(position)

    def move_up(self) -> bool:
        """
        Moves paddle upward
        :return: False if the paddle reaches the top of the screen. True otherwise, after moving the paddle.
        """
        if self.ycor() >= 350:
            return False
        else:
            new_y = self.ycor() + PADDLE_SPEED
            self.goto(self.xcor(), new_y)
            return True

    def move_down(self) -> bool:
        """
        Moves paddle downward.
        :return: False if the paddle reaches the bottom of the screen. True otherwise, after moving the paddle.
        """
        if self.ycor() <= -350:
            return False
        else:
            new_y = self.ycor() - PADDLE_SPEED
            self.goto(self.xcor(), new_y)
            return True
