from turtle import Screen
from paddle import Paddle

sc = Screen()
sc.setup(width=800, height=600)
sc.bgcolor("black")
sc.title("Breakout Game")

paddle = Paddle()

sc.listen()
sc.onkey(paddle.move_r, "Right")
sc.onkey(paddle.move_l, "Left")

sc.exitonclick()
