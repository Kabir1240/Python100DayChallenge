from turtle import Turtle
import random
INITIAL_HEADINGS = [(20, 20), (-20, -20)]


class Ball(Turtle):
    """
    Ball class for the pong game.
    """
    def __init__(self):
        """
        Initializes the ball.
        """
        super().__init__()
        current_heading = random.choice(INITIAL_HEADINGS)
        self.x_move = current_heading[0]
        self.y_move = current_heading[1]
        self.shape("circle")
        self.color("white")
        # move_speed is meant to be used as the argument for time.sleep() during the game
        self.move_speed = 0.0005
        self.penup()

    def speed_up(self) -> None:
        """
        increases ball speed
        :return:
        """
        self.move_speed /= 100

    def slow_down(self) -> None:
        """
        returns the ball speed to the original amount
        :return: None
        """
        self.move_speed = 0.0005

    def move(self) -> None:
        """
        Moves the ball forward
        :return: None
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def contact_floor_ceil(self) -> None:
        """
        Reflect the ball in the y-axis
        :return: None
        """
        self.y_move *= -1

    def contact_paddle(self) -> None:
        """
        Reflects the ball in the x-axis
        :return: None
        """
        self.x_move *= -1
        self.speed_up()

    def to_centre(self) -> None:
        """
        Returns the ball to the origin. Resets its speed as well.
        """
        self.slow_down()
        self.hideturtle()
        self.goto(0, 0)
        self.showturtle()

        self.x_move *= -1
