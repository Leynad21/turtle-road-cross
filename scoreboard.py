from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0


    def show_score(self):
        self.color("Black")
        self.penup()
        self.hideturtle()
        self.setpos(280, 250)
        self.write(f"Score: {self.score} ", move= False, align= "center", font= ("Arial", 18, "normal"))

    def increase_score(self):
        self.score += 1

    def score_zero(self):
        self.score = 0