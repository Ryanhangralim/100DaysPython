from turtle import Turtle
ALIGNTMENT = "center"
FONT = ("Courier", 12, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(arg=f"Score : {self.score}", move=False, align=ALIGNTMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNTMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()