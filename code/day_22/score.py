from turtle import Turtle


class Score(Turtle):
    def __init__(self, font, alignment, position):
        super().__init__()
        self.score = 0
        self.FONT = font
        self.ALIGNMENT = alignment

        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.update()

    def increase_score(self):
        self.score += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"{self.score}", move=False, align=self.ALIGNMENT, font=self.FONT)

    def get_score(self):
        return self.score
