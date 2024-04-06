from turtle import Turtle
from score import Score
ALIGNMENT = 'center'
FONT = ('Courier', 50, 'normal')
PLAYER_SCORE_POSITION = (-50, 320)
CPU_SCORE_POSITION = (50, 320)
BOARD_WIDTH = 5


class Board:
    """
    Board class for pong game. Creates board, manages score and end of the game
    """
    def __init__(self):
        """
        Creates two score objects and board
        """
        self.player_score = Score(FONT, ALIGNMENT, PLAYER_SCORE_POSITION)
        self.cpu_score = Score(FONT, ALIGNMENT, CPU_SCORE_POSITION)
        # create board
        self.create_board()

    def player_score_increase(self) -> None:
        """
        increases player score
        :return: None
        """
        self.player_score.increase_score()

    def cpu_score_increase(self) -> None:
        """
        Increases CPU score
        :return: None
        """
        self.cpu_score.increase_score()

    def create_board(self) -> None:
        """
        Prepares the board
        :return: None
        """

        # create a new turtle
        new_turtle = Turtle()
        new_turtle.shape("square")
        new_turtle.width(BOARD_WIDTH)
        new_turtle.color("white")
        new_turtle.hideturtle()

        # send the turtle to the top of the screen
        new_turtle.penup()
        new_turtle.goto(0, 400)
        new_turtle.setheading(270)
        new_turtle.pendown()

        # creates dashed line in the middle of the board
        while new_turtle.ycor() >= -400:
            new_turtle.fd(30)
            new_turtle.pu()
            new_turtle.fd(20)
            new_turtle.pd()

        # delete the instance of the turtle
        del new_turtle

    def is_game_over(self) -> bool:
        """
        Checks if the game is over. Triggers end game process if it is.
        :return: True if either players have a score equal to 10. False otherwise
        """
        if self.player_score.get_score() >= 10:
            self.game_over("Player")
            return True
        elif self.cpu_score.get_score() >= 10:
            self.game_over("CPU")
            return True
        else:
            return False

    def game_over(self, winner: str) -> None:
        """
        Clears scores. Informs user that the game is over. Informs the user who won.
        :param winner: String that states the winners name
        :return: None
        """
        self.player_score.clear()
        self.cpu_score.clear()
        self.player_score.goto(0, 0)
        self.player_score.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)
        self.player_score.goto(0, -80)
        self.player_score.write(f"{winner} Won!", move=False, align=ALIGNMENT, font=FONT)
