from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")
for _ in range(10):
    timmy.pendown()
    timmy.forward(5)
    timmy.penup()
    timmy.forward(5)

screen = Screen()
screen.exitonclick()