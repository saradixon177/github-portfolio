import turtle
from turtle import *

def square(turtle, length, xloc, yloc):
    turtle.penup()
    turtle.goto(xloc, yloc)
    
    turtle.pendown()
    
    for i in range(4):
        turtle.forward(length)
        turtle.right(90)
  

def main():
    space = Screen()
    t1 = Turtle()
    square(t1, 50, -100, 0)
    t2 = Turtle()
    square(t2, 50, 0, 0)
    t3 = Turtle()
    square(t3, 50, 100, 0)
    
   
    # pick up the pen and go to (-100,0)

    # loop 3 times drawing squares with a length of 50
    # that are 100 pixels apart

main()

