from turtle import Screen
import paddle
from ball import Ball
import time
from scoreboard import Scoreboard


def update_speed(speed):
    return max(0.01, 0.1 - (speed * 0.005))


speed_level = 1
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

ball = Ball()
scoreboard = Scoreboard()
paddle_right = paddle.Paddle()
paddle_right.create_paddle(pos=paddle.RIGHT)
paddle_left = paddle.Paddle()
paddle_left.create_paddle(pos=paddle.LEFT)

screen.listen()
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_right.down, "Down")
screen.onkey(paddle_left.up, "w")
screen.onkey(paddle_left.down, "s")

game_on = True
while game_on:
    time.sleep(update_speed(speed_level))
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_right) < 60 and ball.xcor() > 320 or ball.distance(paddle_left) < 60 and ball.xcor() < -320:
        ball.bounce_x()
        speed_level += 1

    #right side miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        speed_level = 1

    #left side miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        speed_level = 1

screen.exitonclick()
