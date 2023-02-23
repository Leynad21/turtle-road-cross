from turtle import Turtle
import random

#Variables

DISTANCE_MOVE = 10

color_list = ['red', 'pink', 'blue', 'green', 'purple', 'orange', 'yellow']


class Blok():

    def __init__(self):
        self.bloks_list = []


    def gen_blok(self):
        if random.randint(1,6) == 1:
            new_blok = Turtle()
            new_blok.penup()
            new_blok.shape("square")
            new_blok.color(random.choice(color_list))
            new_blok.shapesize(stretch_wid=1, stretch_len=2)
            new_blok.setpos(450, random.randint(-250, 220))
            new_blok.speed()
            self.bloks_list.append(new_blok)




    def blok_move(self):
        for blok in self.bloks_list:
         blok.backward(DISTANCE_MOVE)







