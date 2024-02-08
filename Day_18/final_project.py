from turtle import Screen
import turtle as t
import colorgram
import random

def get_color(image):
    colors = colorgram.extract(image, 30)
    result = []

    for color in colors:
        color_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
        result.append(color_tuple)
    return result

def set_start():
    tim.penup()
    tim.hideturtle()
    tim.setheading(225)
    tim.forward(300)
    tim.setheading(0)
    tim.showturtle()

def draw_line(dot_per_lines):
    for _ in range(dot_per_lines):
        tim.color(random.choice(colors))
        tim.pendown()
        tim.dot(20)
        tim.penup()
        tim.forward(50)

def next_line(dot_per_lines):
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(dot_per_lines*50)
    tim.setheading(0)

def draw_dots(rows, dot_per_lines):
    for _ in range(rows):
        draw_line(dot_per_lines)
        next_line(dot_per_lines)
    tim.hideturtle()

t.colormode(255)
tim = t.Turtle()
tim.shape("turtle")
tim.speed("fastest")
colors = get_color('image.jpg')

set_start()
draw_dots(10, 10)

screen = Screen()
screen.exitonclick()