from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
scoreboard = Scoreboard()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()


screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

left_score = 0
right_score = 0
ball_speed = 0.1
game_is_on = True


def game_over():
    global game_is_on
    game_is_on = False


def restart():
    global left_score, right_score, ball_speed, game_is_on
    scoreboard.left_score = 0
    scoreboard.right_score = 0
    game_is_on = True


screen.onkey(game_over, "q")
screen.onkey(restart, "r")

while game_is_on:
    time.sleep(ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # I could have just used the turtle.distance() method, but I didn't read it, and I don't care to change it

    if (r_paddle.xcor() - 20) == ball.xcor() and r_paddle.ycor() + 50 > ball.ycor() > r_paddle.ycor() - 50:
        ball.change_direction()

    if (l_paddle.xcor() + 20) == ball.xcor() and l_paddle.ycor() + 50 > ball.ycor() > l_paddle.ycor() - 50:
        ball.change_direction()

    if ball.xcor() > 355:
        scoreboard.l_score()
        ball.home()
        r_paddle.goto(350, 0)
        l_paddle.goto(-350, 0)

    if ball.xcor() < -355:
        scoreboard.r_score()
        ball.home()
        r_paddle.goto(350, 0)
        l_paddle.goto(-350, 0)

    if scoreboard.left_score == 5 or scoreboard.right_score == 5:
        game_over()

scoreboard.goto(0, 0)
scoreboard.write(f"The score was {left_score} to {right_score}.\n"
                 f"Press 'r' to play again.", align="center", font=("Courier", 30, "normal"))
screen.exitonclick()
