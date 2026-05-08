#main class, paddle class,score board
from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball 
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))

r_paddle.up()
l_paddle.down()

ball=Ball()
scoreboard=Scoreboard()


game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

#detect collision with wall
    if ball.ball.ycor()>280 or ball.ball.ycor()<-280:
        #needs to bounce 
        ball.bounce_y()
    
#detect collision  with r paddle
    #Detect collision with paddle
    if ball.ball.distance(r_paddle.paddle) < 50 and ball.ball.xcor() > 340 or ball.ball.distance(l_paddle.paddle) < 50 and ball.ball.xcor() < -340:
        ball.bounce_x()

    #Detect R paddle misses
    if ball.ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #Detect L paddle misses:
    if ball.ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()