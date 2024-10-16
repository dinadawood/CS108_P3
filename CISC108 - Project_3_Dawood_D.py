"""
Course: CISC108
Assignment: Project 3
Author: Dina Dawood
"""
# Project 4- Turtle Functions
# If you got help from anyone, please write their emails here:
#  1) acbart@udel.edu
#  2) ...

# Setup turtles; don't need to change these
import turtle
turtle.reset()
turtle.speed(10)
turtle.penup()
turtle.goto(-300, 0)
turtle.pendown()
turtle.speed(3)

###############################################################
# Part 1) Turtle Functions
# Define all of your turtle functions here.

# "H"
def draw_h(x, y):
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(25)
    turtle.backward(50)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(25)
    turtle.backward(50)


# "E"
def draw_e(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(50)
    turtle.backward(50)
    turtle.left(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(45)
    turtle.backward(45)
    turtle.left(90)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(50)

# "L"
def draw_l(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    
# "O"
def draw_o(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(30)
 
# "D"
def draw_d(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.right(90)
    turtle.forward(62)
    turtle.left(90)
    turtle.circle(70,30)
    turtle.left(20)
    turtle.forward(5)
    turtle.circle(30, 170)

# "A"
def draw_a(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(30)
    turtle.backward(30)
    turtle.right(100)
    turtle.forward(50)
    turtle.backward(35)
    turtle.left(100)
    turtle.forward(35)
    turtle.left(100)
    turtle.forward(15)
    turtle.backward(50)
    
# "W"
def draw_w(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.left(105)
    turtle.forward(50)
    turtle.backward(50)
    turtle.right(35)
    turtle.forward(45)
    turtle.right(135)
    turtle.forward(45)
    turtle.left(140)
    turtle.forward(50)
    turtle.backward(50)

###############################################################
# Part 2) Original Words
# Rewrite your original words here, modifying the code below

# Writes "HELLO" at (-300, 0)
x_position = draw_h(-300, 0)
x_position = draw_e(-220, 0)
x_position = draw_l(-140, 0)
x_position = draw_l(-60, 0)
x_position = draw_o(20, 0)

# Writes "DDAWOOD" at (-300, -100)
x_position = draw_d(-300, -100)
x_position = draw_d(-220, -100)
x_position = draw_a(-140, -100)
x_position = draw_w(-60, -100)
x_position = draw_o(20, -100)
x_position = draw_o(100, -100)
x_position = draw_d(180, -100)

###############################################################
# Part 3) New Words
# Write your new words here. Make sure all words are readable.

# Writes "LOW" (-300, -200)
x_position = draw_l(-300, -200)
x_position = draw_o(-220, -200)
x_position = draw_w(-140, -200)

# Writes "HOWL" (0, -200)
x_position = draw_h(0, -200)
x_position = draw_o(80, -200)
x_position = draw_w(160, -200)
x_position = draw_l(240, -200)

# Writes "DAD" (-300, -300)
x_position = draw_d(-300, -300)
x_position = draw_a(-220, -300)
x_position = draw_d(-140, -300)

# Writes "WOOD" (0, -300)
x_position = draw_w(0, -300)
x_position = draw_o(80, -300)
x_position = draw_o(160, -300)
x_position = draw_d(240, -300)

###############################################################
# Wrap-up turtles; don't need to change this
turtle.mainloop()
