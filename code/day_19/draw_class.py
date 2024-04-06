from turtle import Turtle
import random


class Draw(Turtle):
    """
    Draw using a turtle. Class made for etch a sketch
    """
    def __init__(self):
        super().__init__()

    def move_forward(self) -> None:
        """
        moves turtle forward by 10
        :return: None
        """
        self.forward(10)

    def move_backwards(self) -> None:
        """
        Moves turtle backward by 10
        :return: None
        """
        self.backward(10)

    def turn_clockwise(self) -> None:
        """
        Turns turtle clockwise with an angle of 10
        :return: None
        """
        self.right(10)

    def turn_counter_clockwise(self) -> None:
        """
        Turns turtle counter-clockwise with an angle of 10
        :return: None
        """
        self.left(10)

    def random_color(self) -> None:
        """
        Gives turtle a random color
        :return: None
        """
        color = "#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        self.pencolor(color)
