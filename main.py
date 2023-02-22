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

# Body parts
body_parts = []

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
    screen.update()

    # Canvas border collision check
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(2)
        head.goto(0, 0)
        head.direction = "stop"

        # Hiding body parts
        for one_body_part in body_parts:
            one_body_part.goto(1000, 1000)

        # Clearing the list of body parts
        body_parts.clear()

    if head.distance(apple) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        apple.goto(x, y)

        # Adding body parts
        new_body_part = Turtle("square")
        new_body_part.speed(0)
        new_body_part.color("white")
        new_body_part.penup()
        body_parts.append(new_body_part)

    for index in range(len(body_parts) - 1, 0, -1):
        x = body_parts[index - 1].xcor()
        y = body_parts[index - 1].ycor()
        body_parts[index].goto(x, y)

    if len(body_parts) > 0:
        x = head.xcor()
        y = head.ycor()
        body_parts[0].goto(x, y)     
    
    move()

    # Head-to-body collision control
    for one_body_part in body_parts:
        if one_body_part.distance(head) < 20:
            time.sleep(2)
            head.goto(0, 0)
            head.direction = "stop"

            # Hiding body parts
            for one_body_part in body_parts:
                one_body_part.goto(1000, 1000)

            # Clearing the list of body parts
            body_parts.clear()
         
    time.sleep(0.1)
    
screen.exitonclick()