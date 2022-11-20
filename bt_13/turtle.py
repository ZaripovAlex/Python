from turtle import *
from random import randint
from time import *

finish = 0
t1=Turtle()
t1.shape("turtle")
t1.color("orange")
t1.penup()
t1.goto(-400,20)
t1.pendown()
t2=Turtle()
t2.shape("turtle")
t2.color("green")
t2.penup()
t2.goto(-400,60)
t2.pendown()

def razmetka():
    t=Turtle()
    t.penup()
    t.goto(-420,40)
    t.pendown()
    t.goto(0,40)     
      
    for i in range(1,21):
        t.penup()
        t.goto(-400+i*20,140)
        t.pendown()
        t.goto(-400+i*20,-100)
    #t=hidenturtle()
               
    
razmetka()

def catch1(x,y):
    t1.write("АААА!!!!")
    t1.fd(randint(10,15))
    
def catch2(x,y):
    t2.write("УУУУУ!!!!")
    t2.fd(randint(10,15))
t1.onclick(catch1)
t2.onclick(catch2)
while t1.xcor()<finish and t2.xcor()<finish:
    t1.forward(randint(2,7))
    t2.forward(randint(2,7))
    sleep(0.1)