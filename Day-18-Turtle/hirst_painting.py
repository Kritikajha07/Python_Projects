# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle

colors_list=[(211, 163, 117), (247, 232, 235), (139, 49, 105), (164, 169, 38), (243, 80, 57), (98, 194, 210),
 (220, 238, 233), (237, 107, 162), (4, 141, 47), (239, 66, 137), (3, 143, 184), (161, 56, 52), (19, 165, 125),
 (218, 232, 235), (254, 231, 0), (242, 223, 53), (155, 181, 167), (234, 165, 190), (36, 187, 209), (242, 169, 155),
 (136, 214, 225), (151, 214, 184), (106, 45, 89), (191, 190, 194), (5, 118, 34), (137, 41, 32), (86, 38, 81)]



from turtle import Turtle,Screen
import random
tim=Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
turtle.colormode(255)
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots=100

for dot_count in range(1,number_of_dots+1):
    tim.dot(20,random.choice(colors_list))
    tim.forward(50)

    if dot_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(360)

print(tim)

screen=Screen()
screen.exitonclick()
