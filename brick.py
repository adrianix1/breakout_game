from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Brick(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))

    def next_brick_pos(self, i):
        if i <= 18:
            pos_x = -422 + i * 44
            pos_y = 240
        elif 19 <= i <= 36:
            pos_x = -422 + (i-18) * 44
            pos_y = 216
        elif 37 <= i <= 55:
            pos_x = -422 + (i-36) * 44
            pos_y = 192
        brick_pos = (pos_x, pos_y)
        self.setpos(brick_pos)

