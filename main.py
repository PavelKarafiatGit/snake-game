from turtle import Turtle, Screen
import time

screen = Screen()
screen.bgcolor("grey")
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.tracer(False)

# Snake head
head = Turtle("square")
head.color("black")
head.speed(0)
head.penup()
head.goto(0, 0)
head.direction = "stop"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)     

while True:
    move()
    time.sleep(0.1)
    screen.update()


screen.exitonclick()