from turtle import Turtle
START_X_COR = [0, -20, -40]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.segments = []
        for i in range(3):
            self.segments.append(Turtle(shape="square"))
            self.segments[i].color("white")
            self.segments[i].penup()
            self.segments[i].setx(START_X_COR[i])
        self.head = self.segments[0]

    def extend(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.segments[-1].pos())
        self.segments.append(new_segment)
        
    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            self.segments[i].setpos(self.segments[i-1].pos())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    

