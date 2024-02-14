from turtle import Turtle
ALIGNTMENT = "center"
FONT = ("Courier", 12, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.score = 0
        self.get_highscore()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.highscore}", move=False, align=ALIGNTMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_highscore()
        self.update_scoreboard()

    
    def get_highscore(self):
        with open("highscore.txt", mode="r") as file:
            score = int(file.read())
            self.highscore = score


    def update_highscore(self):
        with open("highscore.txt", mode="w") as file:
            file.write(str(self.highscore))


    def add_score(self):
        self.score += 1
        self.update_scoreboard()