from draw_class import Draw
from turtle import Screen


def etch_a_sketch():
    """
    etch a sketch program using turtle graphics
    :return:
    """

    # draw is a turtle instance
    draw = Draw()
    screen = Screen()
    screen.listen()
    screen.onkey(key="w", fun=draw.move_forward)
    screen.onkey(key="s", fun=draw.move_backwards)
    screen.onkey(key="a", fun=draw.turn_counter_clockwise)
    screen.onkey(key="d", fun=draw.turn_clockwise)
    screen.onkey(key="space", fun=draw.random_color)
    screen.onkey(key="c", fun=screen.reset)
    screen.exitonclick()


etch_a_sketch()