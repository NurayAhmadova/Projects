from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("dark olive green")

colors = ["slate blue", "orange red", "gold", "forest green", "blue", "light salmon", "blue violet", "red"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)


def dashed():
    for dash in range(15):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()


screen = Screen()
screen.exitonclick()
