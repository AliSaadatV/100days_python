from turtle import Turtle, Screen
import random
        
timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")
timmy.pensize(10)
timmy.speed(6)

screen = Screen()
screen.colormode(255)

for _ in range(50):
    rotation = random.choice([0, 90, 180, 270])
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    timmy.pencolor(r, g, b)
    timmy.left(rotation)
    timmy.forward(30)


screen.exitonclick()