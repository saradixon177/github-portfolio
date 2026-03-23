import turtle
from turtle import *

def create_colored_triangle(t, length, xloc, yloc, color): 
    t.penup()
    t.goto(xloc, yloc)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill() 
    for i in range(3):
        t.forward(length)
        t.left(120)
    t.end_fill()


def create_square(t, length, xloc, yloc, color):
    t.penup()
    t.goto(xloc, yloc)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill() 
    for i in range(4):
        t.forward(length)
        t.right(90)   
    t.end_fill()  

def create_house(t, length, x, y):
    # Draw the main blue structure
    create_square(t, length, x, y, "cyan")
    
    # FIX 2: Added the roof back in!
    create_colored_triangle(t, length, x, y, "red")

    # To put a door at the bottom, y needs to be lowered by the house length.
    door_length = length * 0.3
    door_x = x + (length * 0.35)
    door_y = y - (length * 0.7) # Moves it to the bottom of the square

    create_square(t, door_length, door_x, door_y, "white")

def create_mountain(t, length, x, y): 
    create_colored_triangle(t, length, x, y, "brown")
    
    cap_length = length * 0.3
    peak_x = x + (length * 0.35) 
    peak_y = y + (length * 0.6)
    
    create_colored_triangle(t, cap_length, peak_x, peak_y, "white")

def main(): 
    screen = Screen()
    screen.bgcolor("skyblue")

    artist = Turtle()
    artist.speed(0) 

    # Draw mountain in the back
    create_mountain(artist, 300, -200, -100)

    # Draw house in the front
    create_house(artist, 100, 50, 0)
    
    screen.exitonclick()

main()