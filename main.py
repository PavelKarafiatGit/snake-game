from turtle import Turtle, Screen
import time
import random

score = 0
highest_score = 0

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

# Score
score_sign = Turtle("square")
score_sign.speed(0)
score_sign.color("yellow")
score_sign.penup()
score_sign.hideturtle()
score_sign.goto(0, 260)
score_sign.write("Score: 0                           Highest score: 0", align="center", font=("Arial", 18))

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
    if head.direction != "down":
        head.direction = "up"
def move_down():
    if head.direction != "up":
        head.direction = "down"
def move_right():
    if head.direction != "left":
        head.direction = "right"
def move_left():
    if head.direction != "right":
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

        # Reset score
        score = 0 
        score_sign.clear()
        score_sign.write(f"Score: {score}                           Highest score: {highest_score}", align="center", font=("Arial", 18))

    # Head collision with an apple - the snake eats the apple
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

        # Score
        score += 10
        if score > highest_score:
            highest_score = score
        score_sign.clear()
        score_sign.write(f"Score: {score}                           Highest score: {highest_score}", align="center", font=("Arial", 18))

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

             # Reset score
            score = 0 
            score_sign.clear()
            score_sign.write(f"Score: {score}                           Highest score: {highest_score}", align="center", font=("Arial", 18))
         
    time.sleep(0.1)
    
screen.exitonclick()