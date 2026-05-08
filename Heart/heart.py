#make a simple colour filled heart shape using Turtle

from turtle import Turtle,Screen
screen=Screen()
tim=Turtle()
tie=Turtle()
tim.speed(1)
tim.pensize(3)

screen.bgcolor("antiquewhite")
tie.color("Red")
tie.hideturtle()
tie.penup()
tie.goto(0,260)

tie.write("Happy Valentine's Day!!", align="center", font=("Brush Script MT", 30, "normal"))
screen.title("Happy Valentine's Day..")
def func():
    for i in range(200):
        tim.right(1)
        tim.forward(1)
       

tim.color("red","darkred")
tim.begin_fill()
tim.left(140)
tim.forward(111.65)
func()
tim.left(120)
func()
tim.forward(111.65)

tim.end_fill()
tim.hideturtle()
screen.exitonclick()