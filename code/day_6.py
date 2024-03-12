# These are solutions for Reebogs World. https://reeborg.ca/index_en.html


# Solution for hurdle 4
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        jump()


# Solution for maze
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if not wall_in_front():
        move()
    elif not wall_on_right():
        turn_right()
    else:
        turn_left()