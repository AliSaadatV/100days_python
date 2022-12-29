from turtle import Turtle, Screen
import random
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    if color.rgb.r < 230 and color.rgb.g < 230 and color.rgb.b < 230:
        rgb_colors.append(tuple(color.rgb))  

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")
timmy.pensize(5)
timmy.speed("normal")

screen = Screen()
screen.colormode(255)


def set_position(n):
    timmy.penup()
    if n % 2 == 0:
        timmy.left(90)
        timmy.forward(20)
        timmy.left(90)
    else:
        timmy.right(90)
        timmy.forward(20)
        timmy.right(90)
    

def draw_line_dots(n_dots):
    for i in range(n_dots):
        timmy.dot(5, random.choice(rgb_colors))
        timmy.penup()
        if i < n_dots-1:
            timmy.forward(20)
            timmy.pendown()


n_line = 5   
n_dots_per_line = 6
for i in range(n_line):
    draw_line_dots(n_dots_per_line)
    set_position(i)

screen.exitonclick()