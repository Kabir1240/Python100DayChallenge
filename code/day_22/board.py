from turtle import Turtle
from score import Score
ALIGNMENT = 'center'
FONT = ('Courier', 50, 'normal')
PLAYER_SCORE_POSITION = (-50, 320)
CPU_SCORE_POSITION = (50, 320)
BOARD_WIDTH = 5


class Board:
    def __init__(self):
        self.player_score = Score(FONT, ALIGNMENT, PLAYER_SCORE_POSITION)
        self.cpu_score = Score(FONT, ALIGNMENT, CPU_SCORE_POSITION)

        self.create_board()

    def player_score_increase(self) -> None:
        self.player_score.increase_score()

    def cpu_score_increase(self) -> None:
        self.cpu_score.increase_score()

    def create_board(self) -> None:
        new_turtle = Turtle()
        new_turtle.shape("square")
        new_turtle.width(BOARD_WIDTH)
        new_turtle.color("white")
        new_turtle.hideturtle()

        new_turtle.penup()
        new_turtle.goto(0, 400)
        new_turtle.setheading(270)
        new_turtle.pendown()

        while new_turtle.ycor() >= -400:
            new_turtle.fd(30)
            new_turtle.pu()
            new_turtle.fd(20)
            new_turtle.pd()

        del new_turtle

    def is_game_over(self) -> bool:
        if self.player_score.get_score() >= 10:
            self.game_over("Player")
            return True
        elif self.cpu_score.get_score() >= 10:
            self.game_over("CPU")
            return True
        else:
            return False

    def game_over(self, winner: str) -> None:
        self.player_score.clear()
        self.cpu_score.clear()
        self.player_score.goto(0, 0)
        self.player_score.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)
        self.player_score.goto(0, -80)
        self.player_score.write(f"{winner} Won!", move=False, align=ALIGNMENT, font=FONT)
