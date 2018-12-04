# Ветка Арины (фигура).
from turtle import *
n = int(input())
d = 500//n
a = (d // (3 ** 0.5))
b = (d //(2 * (3 ** 0.5)))
c = ((b * 2) + a)
e = 500 // c
arina_idealna = a
right(90)
forward(arina_idealna)
right(60)
forward(arina_idealna)
right(60)
forward(arina_idealna)
right(60)
forward(arina_idealna)
right(60)
forward(arina_idealna)
right(60)
forward(arina_idealna)
mainloop()
