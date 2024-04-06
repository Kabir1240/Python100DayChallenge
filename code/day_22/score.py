from turtle import Turtle


class Score(Turtle):
    """
    Score class for pong game. Initialized in the Board class. Keeps score for players.
    """
    def __init__(self, font, alignment, position):
        """
        Initializes score
        :param font: Font to use for the score.
        :param alignment: Alignment to use for the score
        :param position: Position to display the score
        """
        super().__init__()
        self.score = 0
        self.FONT = font
        self.ALIGNMENT = alignment

        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.update()

    def increase_score(self) -> None:
        """
        Increases the score, updates it on the board.
        :return: None
        """
        self.score += 1
        self.update()

    def update(self) -> None:
        """
        Clears previous score and updates the current score on the board.
        :return: None
        """
        self.clear()
        self.write(f"{self.score}", move=False, align=self.ALIGNMENT, font=self.FONT)

    def get_score(self) -> int:
        """
        Returns the current score.
        """
        return self.score
