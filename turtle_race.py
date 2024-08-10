from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the Race? Enter a color: ")
colors = ["red", "green", "blue", "orange", "yellow", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")   # instances of object
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(tim)

if user_bet:
    is_race_on = True

    while is_race_on:
        for turtles in all_turtles:

            if turtles.xcor() > 230:
                is_race_on = False
                winning_color = turtles.pencolor()
                if winning_color == user_bet:
                    print(f"Your {winning_color} Turtle Won! Congratulations!!!!")
                else:
                    print(f"Your {winning_color} Turtle Lost, Didn't Expect that")

            turtles.fd(randint(0, 10))


screen.exitonclick()
