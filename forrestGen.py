#!/bin/python3
import random
import turtle

def draw_tree(turtle, width, height):
    draw_trunk(turtle, width, height)
    draw_leafs(turtle, width, height)


def draw_leafs(turtle, width, height, triangles=3):
    turtle.colormode(225)
    turtle.pencolor(use_color)
    turtle.fillcolor(use_color)

    for i in range(triangles):
        draw_triangle(turtle, width, height)
        height_increase = height/2
        turtle.sety(turtle.ycor() + height_increase)


def draw_trunk(turtle, width, height):
    turtle.color('brown')
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.end_fill()


def draw_triangle(turtle, width, height):
    branch_overhang = height
    triangle_height = 2*height

    turtle.begin_fill()

    x_init, y_init = (turtle.xcor(), turtle.ycor())
    x_middle = x_init + width/2.0
    x_bottom_left = x_init - branch_overhang
    x_bottom_right = x_init + width + branch_overhang
    y_top = y_init + triangle_height

    turtle.goto(x_bottom_left, y_init)
    turtle.goto(x_middle, y_top)
    turtle.goto(x_bottom_right, y_init)
    turtle.goto(x_init, y_init)

    turtle.end_fill()

# forrest never worked

#def create_forest(turtle, width, height):
#    for i in range(15):


turtle.penup()
turtle.setpos(-350,0)
turtle.right(90)

def forest_start():
    turtle.pencolor('skyblue')
    turtle.fillcolor('skyblue')
    turtle.pendown()
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(700)
    turtle.left(90)
    turtle.forward(700)
    turtle.left(90)
    turtle.forward(700)
    turtle.left(90)
    turtle.forward(700)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(30)
    for i in range(6):
        global color_list
        global use_color
        color_list = ['#005600', '#003D00', '#228B22', '#006400']
        use_color = random.choice(color_list)
        R = random.randint(30, 60)
        height = R
        width = R/1.1

        draw_tree(turtle, width, height)
        turtle.penup()
        turtle.right(180)
        turtle.forward(R + R/2)
        turtle.left(90)
        turtle.forward(random.randint(70, 120))
        turtle.pendown()
        for i in range(1, 4):
            use_color = random.choice(color_list)
            print(use_color)
            B = random.randint(8, 20)
            height = B
            width = B/1.1

            draw_tree(turtle, width, height)
            turtle.penup()
            turtle.right(180)
            turtle.forward(B + B/3.5)
            turtle.left(90)
            turtle.forward(random.randint(15, 35))
            turtle.pendown()

forest_start()
turtle.done()
