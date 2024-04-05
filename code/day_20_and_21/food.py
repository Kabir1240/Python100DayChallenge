from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.random_color()
        self.speed("fastest")
        self.refresh()

    def random_color(self):
        colors = ["tomato", "spring green", "medium orchid", "white", "orange", "yellow", "deep sky blue"]
        self.pencolor(random.choice(colors))

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)