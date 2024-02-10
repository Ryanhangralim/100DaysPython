from turtle import Turtle, Screen
MOVE_DISTANCE = 20

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()


    def create_snake(self):
        self.x_axis = 0
        for _ in range(3):
            segment = Turtle()
            segment.shape("square")
            segment.color("white")
            segment.penup()
            segment.goto(self.x_axis, 0)
            self.x_axis -= 20
            self.segments.append(segment)


    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_cor = self.segments[seg_num-1].pos()
            self.segments[seg_num].goto(new_cor)
        self.segments[0].forward(MOVE_DISTANCE)


    def up(self):
        self.segments[0].setheading(90)


    def right(self):
        self.segments[0].setheading(0)


    def down(self):
        self.segments[0].setheading(270)


    def left(self):
        self.segments[0].setheading(180)