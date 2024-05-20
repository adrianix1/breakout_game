from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(0, -250)

    def move_r(self):
        x_cor = self.xcor()
        if x_cor <= 350:
            self.setx(x_cor + 20)

    def move_l(self):
        x_cor = self.xcor()
        if x_cor >= -350:
            self.setx(x_cor - 20)
