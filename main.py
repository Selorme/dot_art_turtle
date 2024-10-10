import turtle
import turtle as turtle_module
from turtle import Screen
import random

turtle_module.colormode(255)
selorme = turtle.Turtle()
selorme.speed("fastest")
selorme.shape("turtle")

color_list = [(244, 229, 50), (202, 7, 33), (237, 228, 2), (193, 67, 24), (221, 151, 81), (36, 210, 91),
              (38, 37, 249), (203, 37, 249)]


def draw_painting():
    for row in range(10):
        for column in range(10):
            selorme.hideturtle()
            selorme.penup()
            selorme.goto(column * 50 - 250, row * 50 - 250)
            selorme.dot(20, random.choice(color_list))


draw_painting()
screen = Screen()
screen.exitonclick()

# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 10)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
