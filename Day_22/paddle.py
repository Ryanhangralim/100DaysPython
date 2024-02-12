from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(position)


    def up(self):
        x_position = self.xcor()
        y_position = self.ycor()
        self.goto(x_position, y_position + 20)


    def down(self):
        x_position = self.xcor()
        y_position = self.ycor()
        self.goto(x_position, y_position - 20)