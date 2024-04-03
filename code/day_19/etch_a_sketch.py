from draw_class import Timmy
from turtle import Screen


def etch_a_sketch():
    timmy = Timmy()
    screen = Screen()
    screen.listen()
    screen.onkey(key="w", fun=timmy.move_forward)
    screen.onkey(key="s", fun=timmy.move_backwards)
    screen.onkey(key="a", fun=timmy.turn_counter_clockwise)
    screen.onkey(key="d", fun=timmy.turn_clockwise)
    screen.onkey(key="space", fun=timmy.random_color)
    screen.onkey(key="c", fun=screen.reset)
    screen.exitonclick()


etch_a_sketch()