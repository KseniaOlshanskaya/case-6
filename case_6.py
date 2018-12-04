# Ветка Ксюши (тесселяция).
import turtle


def tesselation(d, b, n, side_len):

    color1 = get_color_choice(_color_ch)
    color2 = get_color_choice(_color_ch)

    x = -250 + d
    y = 250 + b
    x1 = -250 + d
    x2 = -250 + ((3 * d) / 2)
    counter = 0
    counter2 = 1

    turtle.reset()
    turtle.up()

    for s in range(n):
        counter += 1
        for i in range(n):
            if counter2 % 2 == 0:
                color = color1
            else:
                color = color2
            turtle.up()
            x += d
            turtle.right(90)
            draw_hexagon(x, y, side_len, color)
            counter2 += 1
        if counter % 2 == 0:
            x = x1
        else:
            x = x2
        y = y - (side_len + b)
    turtle.mainloop()
