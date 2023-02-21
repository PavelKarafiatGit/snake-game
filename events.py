from turtle import Turtle, Screen

screen = Screen()
turtle = Turtle("turtle")

def move_forward():
    turtle.forward(20)

# Pressing a key
screen.listen()
screen.onkeypress(move_forward, "d")

screen.exitonclick()