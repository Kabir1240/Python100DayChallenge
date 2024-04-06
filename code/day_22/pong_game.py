import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from board import Board
PLAYER_PADDLE_STARTING_POSITION = (-720, 0)
CPU_PADDLE_STARTING_POSITION = (720, 0)
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 800
MAX_SCORE = 10


def pong_game():
    """
    Main Game logic for pong game using Turtle Graphics.
    """

    # create screen, board and 2 paddles
    screen = Screen()
    player_paddle = Paddle(PLAYER_PADDLE_STARTING_POSITION)
    cpu_paddle = Paddle(CPU_PADDLE_STARTING_POSITION)
    board = Board()
    ball = Ball()

    # initialize screen
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(delay=0)

    # allow user to move paddles up or down
    screen.listen()
    screen.onkeypress(key="Up", fun=player_paddle.move_up)
    screen.onkeypress(key="Down", fun=player_paddle.move_down)

    # game loop
    cpu_paddle_move_up = True
    is_game_over = False
    while not is_game_over:
        # updates screen
        screen.update()
        time.sleep(ball.move_speed)
        ball.move()

        # if someone scores
        if ball.xcor() >= 750:
            ball.to_centre()
            board.player_score_increase()

        elif ball.xcor() <= -750:
            ball.to_centre()
            board.cpu_score_increase()

        # if ball touches ceiling or floor
        if ball.ycor() >= 385 or ball.ycor() <= -385:
            ball.contact_floor_ceil()

        # if ball touches paddle
        if (ball.distance(cpu_paddle) < 50 and ball.xcor() >= 700) or (ball.distance(player_paddle) < 50 and ball.xcor() <= -700):
            ball.contact_paddle()

        # cpu paddle AI. Moves all the way up and then all the way down.
        if cpu_paddle_move_up:
            if not cpu_paddle.move_up():
                cpu_paddle_move_up = False
        else:
            if not cpu_paddle.move_down():
                cpu_paddle_move_up = True

        # check if game is over / end game
        if board.is_game_over():
            break

    screen.exitonclick()


pong_game()