from turtle import Screen
from paddle import Paddle
from ball import Ball
from brick import Brick
from scoreboard import Scoreboard
import time

sc = Screen()
sc.setup(width=800, height=600)
sc.bgcolor("black")
sc.title("Breakout Game")
sc.tracer(0)

paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()

sc.listen()
sc.onkey(paddle.move_r, "Right")
sc.onkey(paddle.move_l, "Left")

brick_list = []
for i in range(1, 56):
    brick = Brick()
    brick.next_brick_pos(i)
    brick_list.append(brick)

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

    # detect paddle collision with the ball
    if ball.distance(paddle) < 50 and ball.ycor() < -220:
        ball.bounce_y()

    # detect paddle miss
    if ball.ycor() < -310:
        paddle.reset_paddle()
        ball.reset_ball()
        if scoreboard.chances > 0:
            scoreboard.take_chance()
        else:
            scoreboard.over()
            game_is_on = False

    # detect collision with a brick
    for a in brick_list:
        if a.distance(ball) < 25:
            a.remove()
            brick_list.remove(a)
            scoreboard.point()
            ball.bounce_y()
            if scoreboard.score % 80:
                ball.move_speed *= 0.9

    if len(brick_list) == 0:
        scoreboard.win()
        game_is_on = False

sc.exitonclick()
