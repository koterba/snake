import turtle
import random
import time

TIME = 0.1

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

def dirup():
    if head.direction != "down":
        head.direction = "up"

def dirdown():
    if head.direction != "up":
        head.direction = "down"

def dirleft():
    if head.direction != "right":
        head.direction = "left"

def dirright():
    if head.direction != "left":
        head.direction = "right"
        
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
    
def is_hitting_tail(direction):
    for segment in segments:
        if direction == "up":
            if segment.xcor() == head.xcor() + 20 and segment.ycor() == head.ycor() + 20:
                return True
                
        if direction == "down":
            if segment.xcor() == head.xcor() and segment.ycor() == head.ycor() - 20:
                return True
                
        if direction == "right":
            if segment.xcor() == head.xcor() + 20 and segment.ycor() == head.ycor():
                return True
                
        if direction == "left":
            if segment.xcor() == head.xcor() - 20 and segment.ycor() == head.ycor():
                return True

        return False
    
    
def temp_move(direction, second_direction = None):
    wn.update()
    time.sleep(TIME)
    prevx, prevy = head.xcor(), head.ycor()

    if direction == "up":
        dirup()
        
    if direction == "down":
        dirdown()
        
    if direction == "right":
        dirright()
        
    if direction == "left":
        dirleft()
        
    move()

    
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 220 or head.ycor() < -290:
        reset()

    if head.distance(food) < 20:
        addfood()
        print("ADDED FOOD")

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()

        segments[0].goto(prevx, prevy)

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
        

        segments[0].goto(prevx, prevy)
    
    for segment in segments:
        if segment.distance(head) < 20:
            reset()
    
    wn.update()
    time.sleep(TIME)
    prevx, prevy = head.xcor(), head.ycor()

    if second_direction == "up":
        dirup()
        
    if second_direction == "down":
        dirdown()
        
    if second_direction == "right":
        dirright()
        
    if second_direction == "left":
        dirleft()
        
    move()

    
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 220 or head.ycor() < -290:
        reset()

    if head.distance(food) < 20:
        addfood()
        print("ADDED FOOD")

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()

        segments[0].goto(prevx, prevy)

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

        segments[0].goto(prevx, prevy)
    
    for segment in segments:
        if segment.distance(head) < 20:
            reset()

def main_move(direction):
    wn.update()
    time.sleep(TIME)
    prevx, prevy = head.xcor(), head.ycor()

    if direction == "up" and head.direction == "down":
        temp_move("right", "up")
        return
    elif direction == "up":
        if is_hitting_tail("up") == True:
            if is_hitting_tail("right") == False:
                main_move("right")
                return
            elif is_hitting_tail("left") == False:
                main_move("left")
                return
        dirup()
        move()
        
    elif direction == "down" and head.direction == "up":
        temp_move("right", "down")
        return
    elif direction == "down":
        if is_hitting_tail("down") == True:
            if is_hitting_tail("right") == False:
                main_move("right")
                return
            elif is_hitting_tail("left") == False:
                main_move("left")
                return
        dirdown()
        move()
        
    elif direction == "right" and head.direction == "left":
        temp_move("down", "right")
        return
    elif direction == "right":
        if is_hitting_tail("right") == True:
            print("about to hit right")
            if is_hitting_tail("up") == False:
                print("is not hitting up")
                main_move("up")
                return
            elif is_hitting_tail("down") == False:
                main_move("down")
                return
        dirright()
        move()
        
    elif direction == "left" and head.direction == "right":
        temp_move("down", "left")
        return
    elif direction == "left":
        if is_hitting_tail("left") == True:
            if is_hitting_tail("up") == False:
                main_move("up")
                return
            elif is_hitting_tail("down") == False:
                main_move("down")
                return
        dirleft()
        move()
        
    

    
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 220 or head.ycor() < -290:
        reset()

    if head.distance(food) < 20:
        addfood()
        print("ADDED FOOD")

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()

        segments[0].goto(prevx, prevy)

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

        segments[0].goto(prevx, prevy)
    
    for segment in segments:
        if segment.distance(head) < 20:
            reset()


while True:
    #prevx, prevy = head.xcor(), head.ycor()

    #move()
    #print("HEAD DIR: ",head.direction)
    
    
    while food.ycor() < head.ycor(): ## down
        main_move("down")

    while food.ycor() > head.ycor(): ## up
        main_move("up")

    while food.xcor() > head.xcor(): ## right
        main_move("right")

    while food.xcor() < head.xcor(): ## left
        main_move("left")



wn.exitonclick()
