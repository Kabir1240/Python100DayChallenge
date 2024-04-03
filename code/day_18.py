import turtle
from turtle import Turtle, Screen
import random
import colorgram


class Draw:
    def __init__(self):
        self.timmy = Turtle()
        self.timmy.shape("turtle")
        self.timmy.pencolor("DarkSlateBlue")
        self.screen = Screen()

    def draw_square(self):
        for _ in range(4):
            self.timmy.forward(100)
            self.timmy.right(90)
        self.reset()

    def draw_dashed(self):
        for _ in range(15):
            self.timmy.fd(10)
            self.timmy.pu()
            self.timmy.fd(10)
            self.timmy.pd()

        draw.reset()

    def draw_shapes(self):
        for i in range(3, 10):
            angle = 360 / i
            for _ in range(i):
                self.timmy.fd(100)
                self.timmy.right(angle)
            self.random_color()

        draw.reset()

    def draw_random_walk(self, length=10, pensize=10, turtle_speed=10, line_size=20):
        directions = [90, 180, 270, 360]

        self.timmy.speed(turtle_speed)
        self.timmy.width(pensize)
        for _ in range(length):
            self.timmy.forward(line_size)
            self.timmy.setheading(random.choice(directions))
            self.random_color()

        self.reset()

    def draw_spirograph(self, radius=100, turtle_speed=10, angle=10):
        self.timmy.speed(turtle_speed)
        n_of_circles = int(360/angle)
        for _ in range(n_of_circles):
            self.timmy.circle(radius)
            self.timmy.right(angle)
            self.random_color()
        self.reset()

    def draw_hirst_spot_painting(self, height=5, width=5, radius=25, space=50, turtle_speed=50, image="day_18_image.jpg"):
        self.screen.colormode(255)
        colors = colorgram.extract(image, 20)
        self.timmy.speed(turtle_speed)

        self.timmy.hideturtle()
        self.timmy.pu()
        self.timmy.goto(-200, -200)
        # self.timmy.pd()

        for _ in range(height):
            for _ in range(width):
                new_color = random.choice(colors).rgb
                self.timmy.pencolor(new_color.r, new_color.g, new_color.b)
                self.timmy.fillcolor(new_color.r, new_color.g, new_color.b)
                # self.timmy.begin_fill()
                self.timmy.dot(radius)
                # self.timmy.end_fill()
                # self.timmy.pu()
                self.timmy.fd(space)
                # self.timmy.pd()
            # self.timmy.pu()
            self.timmy.goto(-200, self.timmy.pos()[1] + space)
            # self.timmy.pd()


    def random_color(self):
        color = "#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        self.timmy.pencolor(color)

    def done_drawing(self):
        self.screen.exitonclick()

    def reset(self):
        self.screen.reset()
        self.random_color()


draw = Draw()
# image="day_18_image.jpg"
# draw.draw_square()
# draw.draw_dashed()
# draw.draw_shapes()
# draw.draw_random_walk(length=100, line_size=20)
# draw.draw_spirograph(turtle_speed=50, angle=2)
# draw.draw_hirst_spot_painting()
draw.done_drawing()
