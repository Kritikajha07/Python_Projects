from turtle import Turtle, Screen
import random
tim = Turtle()
# random colour generation
def colour():
     r = random.random()
     g = random.random()
     b = random.random()

     tim.color(r, g, b)

# for a spirograph
for i in range(38):
    colour()
    tim.speed("fastest")
    tim.circle(75)
    tim.distance(10, 10)
    tim.forward(10)
    tim.right(10)
#def random path
# def path():
#     x=random.random()
#     y=random.random()
#     tim.goto(x,y)
#     tim.forward(x,y)


#generate random lines with size specification and in random directions

# import turtle
# import random
#
# tim = Turtle()
#
# def random_color():
#     r=random.randint(0,255)
#     g=random.randint(0,255)
#     b=random.randint(0,255)
#
#     random_color=(r,g,b)
#     return random_color
#
#
# tim.color(random_color())

# screen = turtle.Screen()
# # pen = turtle.Turtle()
# # pen.shape("arrow")
# # pen.speed(0)  # Fastest speed for instant drawing
# # pen.pensize(10)
# #
# # # Define a list of directions (in degrees)
# # directions = [0, 90, 180, 270]  # North, East, South, West
# #
# # # Generate a random path with 200 steps
# # for _ in range(200):
# #     # pen.color(random.choice(["red", "blue", "green", "yellow", "purple"]))  # Random color
# #     colour()
# #     pen.setheading(random.choice(directions))  # Random direction
# #     pen.forward(20)
#     # Move forward 20 units

screen = Screen()
screen.exitonclick()



#create different types of shapes using turtle

# # print(tim.pensize())
# # tim.color("DarkSlateGray")
#
# def colour():
#     r = random.random()
#     g = random.random()
#     b = random.random()
#
#     tim.color(r, g, b)
#
#
# # print(tim.pendown())
# # print(tim.dot(10,"DarkSlateGray"))
# # for _ in range(10):
# #     tim.forward(10)
# #     tim.penup()
# #     tim.forward(10)
# #     tim.pendown()
# #
# should_continue = True
#
# while should_continue:
#     colour()
#     for triangle in range(1):
#         tim.left(60)
#         tim.backward(100)
#         tim.left(60)
#         tim.forward(100)
#         tim.left(60)
#         tim.backward(100)
#
#     colour()
#     for square in range(4):
#         tim.right(90)
#         tim.backward(100)
#
#     colour()
#     for hexagon in range(5):
#         tim.right(60)
#         tim.backward(100)
#
#     tim.right(240)
#     colour()
#
#     for pentagon in range(5):
#         tim.forward(100)
#         tim.right(72)
#
#     colour()
#     for heptagon in range(7):
#         tim.forward(100)
#         tim.right(51.43)
#
#     colour()
#     for octagon in range(8):
#         tim.forward(100)
#         tim.right(45)
#
#     colour()
#     for nonagon in range(9):
#         tim.forward(100)
#         tim.right(40)
#
#     colour()
#     for decagon in range(10):
#         tim.forward(100)
#         tim.right(36)
#
#     should_continue=False
#
#
#
# # tim.shape("turtle")
# # tim.color("DarkSlateGrey")
# # # tim.forward(100)
# # # tim.right(90)
# # # tim.forward(100)
# # # tim.right(90)
# # # tim.forward(100)
# # # tim.right(90)
# # # tim.forward(100)
# #
# #
# # for _ in range(4):
# #     tim.forward(100)
# #     tim.right(90)



# a hero module which one can download

# # import heroes as h
# # print(h.gen)


