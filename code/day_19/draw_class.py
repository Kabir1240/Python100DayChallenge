from turtle import Turtle, Screen
import random


class Timmy:
    def __init__(self):
        self.timmy = Turtle()

    def move_forward(self):
        self.timmy.forward(10)

    def move_backwards(self):
        self.timmy.backward(10)

    def turn_clockwise(self):
        self.timmy.right(10)

    def turn_counter_clockwise(self):
        self.timmy.left(10)

    def random_color(self):
        color = "#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        self.timmy.pencolor(color)
