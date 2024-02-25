import random
import turtle
import time
delay = 0.15
 
screen = turtle.Screen()
screen.title('Snake Game')
screen.bgcolor('lightgreen')
screen.setup(width=600, height=600)
screen.tracer(0)
 
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 100)
head.direction = "stop"
 
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.shapesize(0.80, 0.80)
food.goto(0, 0)
 
tails = []
point = 0
 
writee = turtle.Turtle()
writee.speed(0)
writee.shape("square")
writee.color("white")
writee.penup()
writee.hideturtle()
writee.goto(0, 260)
writee.write("Point: {}".format(point), align="center", font=("Courier", 24, "normal"))
 
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
 
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
 
 
 
 
 
def go_right():
    if head.direction != "left":
        head.direction = "right"
def go_left():
    if head.direction != "right":
        head.direction = "left"
 
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_right, "Right")
screen.onkey(go_left, "Left")
 
while True:
    screen.update()
 
    if head.xcor() > 300 or head.xcor() < -300 or head.ycor() > 300 or head.ycor() < -300:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
 
        for kuyruk in tails:
            kuyruk.goto(1000, 1000)
        tails = []
 
        point = 0
        delay = 0.1
 
        writee.clear()
        writee.write("Point: {}".format(point), align="center", font=("Courier", 24, "normal"))
 
    if head.distance(food) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        food.goto(x, y)
 
        yeni_kuyruk = turtle.Turtle()
        yeni_kuyruk.speed(0)
        yeni_kuyruk.shape("square")
        yeni_kuyruk.color("white")
        yeni_kuyruk.penup()
        tails.append(yeni_kuyruk)
 
        delay -= 0.001
 
        point = point + 10
        writee.clear()
        writee.write("Point: {}".format(point), align="center", font=("Courier", 24, "normal"))
 
    for index in range(len(tails) - 1, 0, -1):
        x = tails[index - 1].xcor()
        y = tails[index - 1].ycor()
        tails[index].goto(x, y)
 
    if len(tails) > 0:
        x = head.xcor()
        y = head.ycor()
        tails[0].goto(x, y)
 
    move()
 
    for segment in tails:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in tails:
                segment.goto(1000, 1000)
            tails = []
            point = 0
            writee.clear()
            writee.write('Point: {}'.format(point), align='center', font=('Courier', 24, 'normal'))
            hiz = 0.15
 
    time.sleep(delay)
