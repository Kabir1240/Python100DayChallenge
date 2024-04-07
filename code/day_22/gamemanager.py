from turtle import Turtle
from create_board import CreateBoard
ALIGNMENT = 'center'
FONT = ('Courier', 50, 'normal')
PLAYER_SCORE_POSITION = (-50, 320)
CPU_SCORE_POSITION = (50, 320)


class GameManager(Turtle):
    """
    Board class for pong game. Creates board, manages score and end of the game
    """
    def __init__(self):
        """
        Initializes settings for turtle
        """
        super().__init__()
        # score data
        self.player_score = 0
        self.cpu_score = 0

        # initial turtle settings
        self.speed("fastest")
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update()

        # creates the board
        create_board = CreateBoard()
        create_board.create_board()

    def player_score_increase(self) -> None:
        """
        increases player score
        :return: None
        """
        self.player_score += 1
        self.update()

    def cpu_score_increase(self) -> None:
        """
        Increases CPU score
        :return: None
        """
        self.cpu_score += 1
        self.update()

    def update(self) -> None:
        """
        Clears previous score and updates the current score on the board.
        :return: None
        """
        self.clear()
        self.goto(PLAYER_SCORE_POSITION)
        self.write(f"{self.player_score}", move=False, align=ALIGNMENT, font=FONT)
        self.goto(CPU_SCORE_POSITION)
        self.write(f"{self.cpu_score}", move=False, align=ALIGNMENT, font=FONT)

    def is_game_over(self) -> bool:
        """
        Checks if the game is over. Triggers end game process if it is.
        :return: True if either players have a score equal to 10. False otherwise
        """
        if self.player_score >= 10:
            self.game_over("Player")
            return True
        elif self.cpu_score >= 10:
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
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)
        self.goto(0, -80)
        self.write(f"{winner} Won!", move=False, align=ALIGNMENT, font=FONT)
