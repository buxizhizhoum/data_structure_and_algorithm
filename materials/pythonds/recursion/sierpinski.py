#!/usr/bin/python
# -*- coding: utf-8 -*-

import turtle


def draw_triangle(turtle_obj, point, color):
    """
    point: x, y
           x, y
           x, y
    :param turtle_obj:
    :param point:
    :param color:
    :return:
    """
    turtle_obj.goto(point[0][0], point[0][1])
    turtle_obj.fillcolor(color)
    turtle_obj.begin_fill()
    turtle_obj.goto(point[1][0], point[1][1])
    turtle_obj.goto(point[2][0], point[2][1])
    turtle_obj.goto(point[0][0], point[0][1])
    turtle_obj.end_fill()


def get_mid(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2


def sierpinski(turtle_obj, points, degree):
    color_map = ["red", "orange", "green", "yellow", "pink", "violet", "blue"]
    draw_triangle(turtle_obj, points, color_map[degree])

    if degree > 0:

        # point_list_0 = [get_mid(points[2], points[0]), get_mid(points[0], points[1]), get_mid(points[1], points[2])]
        # sierpinski(turtle_obj, point_list_0, degree - 1)

        point_list_1 = [points[0], get_mid(points[0], points[1]), get_mid(points[0], points[2])]
        sierpinski(turtle_obj, point_list_1, degree - 1)

        point_list_2 = [get_mid(points[1], points[2]), points[1], get_mid(points[1], points[0])]
        sierpinski(turtle_obj, point_list_2, degree - 1)

        point_list_3 = [get_mid(points[2], points[0]), get_mid(points[2], points[1]), points[2]]
        sierpinski(turtle_obj, point_list_3, degree - 1)


def main():
    turtle_obj = turtle.Turtle()
    window = turtle.Screen()
    points = [[-100, -50], [0, 100], [100, -50]]
    sierpinski(turtle_obj, points, 3)
    window.exitonclick()


if __name__ == "__main__":
    main()
