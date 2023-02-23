from turtle import Turtle
from scoreboard import Scoreboard

# Variables

DISTANCE_MOVE = 20


class Turt(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.setpos(0, -280)
        self.setheading(90)
        self.fininshed = False

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + DISTANCE_MOVE)

    def go_left(self):
        self.goto(self.xcor() - DISTANCE_MOVE, self.ycor())

    def go_right(self):
        self.goto(self.xcor() + DISTANCE_MOVE, self.ycor())

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - DISTANCE_MOVE)

    def turtle_crossed(self):
        if self.ycor() > 280:
            print("You did it!")
            self.fininshed = True
            self.goto(0, -280)

