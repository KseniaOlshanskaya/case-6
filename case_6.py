# Ветка Ксюши (тесселяция).
import turtle


def tesselation(d, b, n, side_len):
    _color_ch = ''
    color1 = get_color_choice(_color_ch)
    color2 = get_color_choice(_color_ch)

    x = -250 + d + (d / 2)
    y = 250 + b
    x1 = -250 + ((3 * d) / 2)
    x2 = -250 + d
    counter = 0
    counter2 = 1

    turtle.reset()
    turtle.up()

    for s in range(n):
        counter += 1
        for i in range(n):
            if counter == 1 or counter == 2 or counter == 5 or counter == 6 or counter == 9 \
                or counter == 10 or counter == 13 or counter == 14 or counter == 17 or counter == 18:
                if counter2 % 2 != 0:
                    color = color1
                else:
                    color = color2
            elif counter == 3 or counter == 4 or counter == 7 or counter == 8 or counter == 11 \
                or counter == 12 or counter == 15 or counter == 16 or counter == 19 or counter == 20:
                if counter2 % 2 != 0:
                    color = color2
                else:
                    color = color1
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


def main():
    _num_hex = 0
    _color_ch = ''
    N = get_num_hexagons(_num_hex)
    hexagon(N)

if __name__ == "__main__":
    main()