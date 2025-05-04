from turtle import Screen
import time
from paddle import paddle
from Ball import ball
from scoreboard import Scoreboard
from border import Border

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

right_paddle = paddle((350, 0))
left_paddle = paddle((-350, 0))
# right_paddle.side('right')
# left_paddle.side('left')
ball = ball()
scoreboard = Scoreboard()
border = Border()

screen.listen()
screen.onkey(right_paddle.move_paddle_up, "Up")
screen.onkey(right_paddle.move_paddle_down, "Down")
screen.onkey(left_paddle.move_paddle_up, "w")
screen.onkey(left_paddle.move_paddle_down, "s")

lets_pong = True
while lets_pong:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()
    # detect collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()
    # detect when paddle misses
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point()
        scoreboard.update_scoreboard()

    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_point()
        scoreboard.update_scoreboard()

    # to end game and declare winner.
    if scoreboard.l_score == 10:
        scoreboard.left_winner()
        lets_pong = False
        screen.exitonclick()

    if scoreboard.r_score == 10:
        scoreboard.right_winner()
        lets_pong = False
        screen.exitonclick()

