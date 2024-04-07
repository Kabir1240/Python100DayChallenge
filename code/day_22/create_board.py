from turtle import Turtle
BOARD_WIDTH = 5

class CreateBoard(Turtle):
    """
    Creates the board outline for pong game
    """
    def __init__(self):
        """
        sets Turtle to required settings.
        """
        super().__init__()
        self.shape("square")
        self.width(BOARD_WIDTH)
        self.color("white")
        self.speed("fastest")
        self.hideturtle()

        # sends turtle to appropriate location
        self.penup()
        self.goto(0, 400)
        self.setheading(270)
        self.pendown()

    def create_board(self) -> None:
        """
        Prepares the board
        :return: None
        """
        while self.ycor() >= -400:
            self.fd(30)
            self.pu()
            self.fd(20)
            self.pd()
