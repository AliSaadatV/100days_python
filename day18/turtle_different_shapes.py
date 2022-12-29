from turtle import Turtle, Screen
import random

def draw_shape(n):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    timmy.pencolor(r, g, b)
    for _ in range(n):
        timmy.forward(50)
        timmy.right(360/n)

        
timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")

screen = Screen()
screen.colormode(255)

for i in range(3, 11):
    draw_shape(i)


screen.exitonclick()