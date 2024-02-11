from turtle import Turtle, Screen
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        self.x_axis = 0
        for _ in range(3):
            next_pos = (self.x_axis, 0)
            self.add_segment(next_pos)
            self.x_axis -= 20

    def add_segment(self, position):
        segment = Turtle()
        segment.shape("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_cor = self.segments[seg_num-1].pos()
            self.segments[seg_num].goto(new_cor)
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if(self.head.heading() != DOWN):
            self.head.setheading(UP)


    def right(self):
        if(self.head.heading() != LEFT):
            self.head.setheading(RIGHT)


    def down(self):
        if(self.head.heading() != UP):
            self.head.setheading(DOWN)


    def left(self):
        if(self.head.heading() != RIGHT):
            self.head.setheading(LEFT)