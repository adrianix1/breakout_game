from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

sc = Screen()
sc.setup(width=800, height=600)
sc.bgcolor("black")
sc.title("Breakout Game")
sc.tracer(0)

paddle = Paddle()
ball = Ball()

sc.listen()
sc.onkey(paddle.move_r, "Right")
sc.onkey(paddle.move_l, "Left")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    sc.update()
    ball.ball_moving()

    # detect collision with top wall
    if ball.ycor() > 280:
        ball.bounce_y()

    # detect collision with left and right wall
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

sc.exitonclick()
