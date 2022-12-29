from turtle import Turtle, Screen
import random
        
timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")
timmy.pensize(5)
timmy.speed("normal")

screen = Screen()
screen.colormode(255)

for _ in range(24):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    timmy.pencolor(r, g, b)
    timmy.left(15)
    timmy.circle(75)

screen.exitonclick()