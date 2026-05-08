# from turtle import Turtle,Screen
# tim=Turtle()
# screen = Screen()
#
#
# def move_forwards():
#     tim.forward(50)
#
# def move_backwards():
#     tim.backward(50)
#
# def move_left():
#     tim.left(10)
#
# def move_right():
#     tim.right(10)
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
# screen.listen()
# screen.onkey(key="w",fun=move_forwards)
# screen.onkey(key="s",fun=move_backwards)
# screen.onkey(key="a",fun=move_left)
# screen.onkey(key="d",fun=move_right)
# screen.onkey(key="c",fun=clear)
# screen.exitonclick()
import turtle
from turtle import Turtle,Screen
import random
is_race_on=False
screen = Screen()
screen.setup(500,400)
user_bet=screen.textinput(title="Make your bet..",prompt="Which turtle will win the race? Enter a color:- ")
print(user_bet)

colors=["red","yellow","blue","green","purple","pink"]
y_positions=[-70,-40,-10,20,50,80]

all_turtles=[]

for turtle_index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"You've Won!! {winning_color} wins!!")
            else:
                print(f"You've Lose!! {winning_color} wins!!")
        ran_distance=random.randint(0,10)
        turtle.forward(ran_distance)


screen.exitonclick()