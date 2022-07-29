from ast import While
from pickle import TRUE
import turtle
wn = turtle.Screen()
wn.title("Pong ")
wn.bgcolor("Black")
wn.setup(width=800 , height= 600)
wn.tracer(0)

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_len=1 ,stretch_wid=5)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)

#Score
score_a=0
score_b=0



#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_len=1 ,stretch_wid=5)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)



#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.shapesize
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = 0.1

#Pen
Pen = turtle.Turtle()
Pen.speed(0)
Pen.color("white")
Pen.penup()
Pen.hideturtle()
Pen.goto(0,260)
Pen.write("Player A Score:0  Player B Score:0" , align="center" , font=("Courier", 15, "normal"))

#Def functions
def paddle_a_up():
    y= paddle_a.ycor()
    y = y +20
    paddle_a.sety(y)

def paddle_a_down():
    y= paddle_a.ycor()
    y = y -20
    paddle_a.sety(y)

def paddle_b_up():
    y= paddle_b.ycor()
    y = y +20
    paddle_b.sety(y)

def paddle_b_down():
    y= paddle_b.ycor()
    y = y -20
    paddle_b.sety(y)

#Keyboard Bindings
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")





#Main game Loop
while True:
    wn.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    ##BorderChecking 
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy = ball.dy*-1


    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx = ball.dx*-1
        score_a= score_a+1
        Pen.clear()
        Pen.write("Player A Score:{}   Player B Score:{}".format(score_a,score_b) , align="center" , font=("Courier", 15, "normal"))

    
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy = ball.dy*-1

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx = ball.dx*-1
        score_b = score_b+1
        Pen.clear()
        Pen.write("Player A Score:{}   Player B Score:{}".format(score_a,score_b) , align="center" , font=("Courier", 15, "normal"))



    #Ball Collisions
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx*=-1

    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx*=-1


    #AI

    if paddle_b.ycor() < ball.ycor() and abs( paddle_b.ycor() - ball.ycor()) >10:
       paddle_b_up()
    elif paddle_b.ycor()>ball.ycor()and abs( paddle_b.ycor() - ball.ycor()) >10:
        paddle_b_down()
    

