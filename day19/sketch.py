from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Choose a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = {}
for i in range(6):
    turtles["tim" + str(i)] = Turtle(shape="turtle")
    turtles["tim" + str(i)].color(colors[i])
    turtles["tim" + str(i)].penup()
    turtles["tim" + str(i)].goto(x=-230, y=-100 + 30*i)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        turtles[turtle].forward(random.randint(0, 10))
        if turtles[turtle].xcor() >= 230:
            is_race_on = False
            winner = turtles[turtle].pencolor()
            break

if user_bet == winner:
    print(f"The winner is {winner}. You won!")
else:
    print(f"The winner is {winner}. You lost!")

screen.exitonclick()
