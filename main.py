import turtle
import random
import time

wn = turtle.Screen()
wn.title("alan cool snake game")
wn.setup(width = 600, height = 600)
wn.bgcolor("black")
wn.tracer(0)

head = turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0,0)
head.speed(0)
head.direction = "Stop"

food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("orange")
food.penup()
food.goto(0,100)

score = 0

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write(f"Score : {score}", align="center", font=("Iosevka", 24))

wn.listen()

can_move = True

def dirup():
    global can_move
    if can_move == True:
        if head.direction != "down":
            head.direction = "up"
            can_move = False

def dirdown():
    global can_move
    if can_move == True:
        if head.direction != "up":
            head.direction = "down"
            can_move = False

def dirleft():
    global can_move
    if can_move == True:
        if head.direction != "right":
            head.direction = "left"
            can_move = False

def dirright():
    global can_move
    if can_move == True:
        if head.direction != "left":
            head.direction = "right"
            can_move = False
        
def addtail():
    addfood()

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
        
play = True
def pause():
    global play
    if play == True:
        play = False
    elif play == False:
        play == True

wn.onkeypress(dirup, "w")
wn.onkeypress(dirdown, "s")
wn.onkeypress(dirleft, "a")
wn.onkeypress(dirright, "d")
wn.onkeypress(dirup, "Up")
wn.onkeypress(dirdown, "Down")
wn.onkeypress(dirleft, "Left")
wn.onkeypress(dirright, "Right")


wn.onkeypress(addtail, "f")
wn.onkeypress(pause, "p")

segments = []

grid = turtle.Turtle()
grid.speed(0)
grid.color("#282828")
x = -290
for ctr in range(600 // 20):  ## draw 10 lines
    grid.penup()
    grid.goto(x, 230)
    grid.pendown()
    grid.goto(x, -290)
    grid.penup()
    x += 20

y = -290
for _ in range(27):
    grid.penup()
    grid.goto(290, y)
    grid.pendown()
    grid.goto(-290, y)
    grid.penup()
    grid.hideturtle()
    y += 20 
tail_colour = 0
def addfood():
    global tail_colour, score
    x = random.randrange(-240, 240, 20)
    y = random.randrange(-240, 240, 20)
    food.goto(x, y)
    score += 1
    pen.clear()
    pen.write(f"Score : {score}", align="center", font=("Iosevka", 24))

    tail = turtle.Turtle()
    tail.shape("square")
    if tail_colour % 5 == 0:
        #tail.color("#282828")
        tail.color("white")
        tail_colour += 1
    else:
        tail.color("white")
        tail_colour += 1
    tail.speed(0)
    tail.penup()
    segments.append(tail)
    
def reset():
    global score
    pen.clear()
    score = 0
    pen.write(f"Score : {score}", align="center", font=("Iosevka", 24))
        
    head.goto(0,0)
    head.direction = "stop"
    for segment in segments:
        segment.goto(1000,1000)
    segments.clear()



while True:
    wn.update()
    time.sleep(0.1)
    prevx, prevy = head.xcor(), head.ycor()
    if play:
        move()
        can_move = True

        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 220 or head.ycor() < -290:
            reset()

        if head.distance(food) < 20:
            addfood()

        for index in range(len(segments) - 1, 0, -1):
            print(index)
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x,y)

        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()

            segments[0].goto(prevx, prevy)
        
        for segment in segments:
            if segment.distance(head) < 20:
                reset()

wn.exitonclick()
