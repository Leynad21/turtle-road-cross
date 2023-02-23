from turtle import Screen
from turtle_gen import Turt
from blockgenerator import Blok
from scoreboard import Scoreboard
import time

#Variables

#time
T = 0.1


screen = Screen()
screen.setup(width=700, height=600)
screen.bgcolor("White")
screen.title("My first Turtle road cross game")
screen.tracer(0)

turt = Turt()
blok_generator = Blok()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(turt.go_up, "w")
screen.onkey(turt.go_left, "a")
screen.onkey(turt.go_right, "d")
screen.onkey(turt.go_down, "s")
screen.onkey(turt.go_up, "Up")
screen.onkey(turt.go_left, "Left")
screen.onkey(turt.go_right, "Right")
screen.onkey(turt.go_down, "Down")


game_is_one = True
while game_is_one:
    screen.update()
    time.sleep(T)
    scoreboard.clear()
    turt.fininshed = False
    scoreboard.show_score()

    blok_generator.gen_blok()
    blok_generator.blok_move()
    turt.turtle_crossed()
    for blok in blok_generator.bloks_list:
        if blok.distance(turt) < 20 :
            turt.goto(0, -280)
            print("You got killed")
            T = 0.1
            scoreboard.score_zero()
    if turt.fininshed:
        scoreboard.increase_score()
        T *= 0.9














screen.exitonclick()