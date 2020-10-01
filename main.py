import turtle
import time
import random

delay = 0.08
speed = 20
body = []
score=0

#Set up screen
window = turtle.Screen()
window.title("Snake Game by @omar1slam")
window.bgcolor("black")
window.setup(width=600,height=600)
window.tracer(0)

#Snake head
head = turtle.Turtle()
head.shape("circle")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Food
food = turtle.Turtle()
food.shape("square")

food.color("red")
food.penup()
food.goto(50,-200)
food.direction = "stop"

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0,150)

#Funcctions
def kill():
    global  score
    pen.goto(0, 150)
    pen.write("Game Over", align="center", font=("Courier", 28, "normal"))
    pen.goto(0, 100)
    pen.write("Score: {}".format(score), align="center", font=("Courier", 22, "normal"))
    time.sleep(5)
    for b in body:
        b.goto(1000, 1000)
    body.clear()
    head.goto(0, 0)
    head.direction = "stop"
    pen.clear()
    score = 0

def move():

    if head.direction == "up":
        y = head.ycor()
        head.sety(y + speed)


    if head.direction == "down":
        y = head.ycor()
        head.sety(y - speed)


    if head.direction == "right":
        x = head.xcor()
        head.setx(x + speed)


    if head.direction == "left":
        x = head.xcor()
        head.setx(x - speed)

def go_up():
    if head.direction != "down":
        head.direction  = "up"

def go_down():
    if head.direction != "up":
        head.direction  = "down"

def go_right():
    if head.direction != "left":
        head.direction  = "right"

def go_left():
    if head.direction != "right":
         head.direction  = "left"

#key bindings
window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_right, "Right")
window.onkeypress(go_left, "Left")



#Game loop
while True:
    window.update()

    if (head.xcor() == 280) or (head.xcor() == -280) or (head.ycor() == 280) or (head.ycor() == -280):
        kill()

    if head.distance(food) < 20:
        x = random.randint(-260,260)
        y = random.randint(-260,260)
        food.goto(x,y)
        new_part = turtle.Turtle()
        new_part.speed(0)
        new_part.shape("square")
        new_part.color("white")
        new_part.penup()
        body.append(new_part)
        score = score + 10

    for i in range(len(body)-1,0,-1):
        x = body[i-1].xcor()
        y = body[i-1].ycor()
        body[i].goto(x,y)


    if len(body)>0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto((x,y))

    if len(body)>1:
        for j in range(1,len(body)):
            if (head.distance(body[j])<10):
                kill()
                break

    move()
    time.sleep(delay)

window.mainloop()