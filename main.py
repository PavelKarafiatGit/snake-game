from turtle import Turtle, Screen
import time
import random

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

# Apple
apple = Turtle("circle")
apple.color("red")
apple.penup()
apple.goto(100, 100)

# Functions
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

def move_up():
    head.direction = "up"
def move_down():
    head.direction = "down"
def move_right():
    head.direction = "right"
def move_left():
    head.direction = "left"

# Pressing a key
screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_right, "d")
screen.onkeypress(move_left, "a")

# Main loop
while True:
    move()
    if head.distance(apple) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        apple.goto(x, y)
    time.sleep(0.1)
    screen.update()


screen.exitonclick()