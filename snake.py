from turtle import Turtle
positions = [(0,0),(-20,0),(-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for position in positions:
            self.add_segment(position)

    def add_segment(self,position):
        segment = Turtle('square')
        segment.color('white')
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg-1].xcor()
            new_y = self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x,new_y)
        self.segments[0].forward((20))

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)
        else:
            pass

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)
        else:
            pass
    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)
        else:
            pass
    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
        else:
            pass
