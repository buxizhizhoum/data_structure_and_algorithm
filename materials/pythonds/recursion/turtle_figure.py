#!/usr/bin/python
# -*- coding: utf-8 -*-
import turtle


def draw_spiral(turtle_obj, line_len):
    if line_len > 0:
        turtle_obj.forward(line_len)
        turtle_obj.right(90)
        draw_spiral(turtle_obj, line_len - 1)


def tree(turtle_obj, line_len):
    if line_len > 0:
        turtle_obj.forward(line_len)
        turtle_obj.right(20)
        tree(turtle_obj, line_len - 15)
        turtle_obj.left(40)
        tree(turtle_obj, line_len - 15)
        turtle_obj.right(20)
        turtle_obj.backward(line_len)


def main():
    turtle_obj.left(90)
    turtle_obj.up()
    turtle_obj.color("green")
    turtle_obj.backward(100)
    turtle_obj.down()

    tree(turtle_obj, 100)


if __name__ == "__main__":
    turtle_obj = turtle.Turtle()
    window = turtle.Screen()

    # draw_spiral(turtle_obj, 100)
    # tree(turtle_obj, 100)
    main()
    window.exitonclick()


