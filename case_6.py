# Ветка Арины (фигура).
from turtle import *
def get_num_hexagon(n):
    d = 500 / n
    side_len = (d / (3 ** 0.5))
    b = (d / (2 * (3 ** 0.5)))
    c = ((b * 2) + side_len)
    x = -250 + d
    y = 250 + b
    return d, side_len, b, c, x, y
def draw_hexagon(x, y, side_len, color):
    turtle.goto(x, y)
    turtle.down()
    turtle.speed()
    turtle.color(color)
    turtle.begin_fill()
    turtle.forward(side_len)
    turtle.right(60)
    turtle.forward(side_len)
    turtle.right(60)
    turtle.forward(side_len)
    turtle.right(60)
    turtle.forward(side_len)
    turtle.right(60)
    turtle.forward(side_len)
    turtle.right(60)
    turtle.forward(side_len)
    turtle.left(30)
    turtle.end_fill()
