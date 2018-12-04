import turtle
from ru_local import *

def get_num_hexagons(_num_hex):
    while True:
        _num_hex = input(NUMBER)
        try:
            _num_hex = int(_num_hex)
            if _num_hex < 4:
                _num_hex = input(RIGHTNUMBER)
                break
            if _num_hex > 20:
                _num_hex = input(RIGHTNUMBER)
                break
        except ValueError:
            print('{} - {}'.format(_num_hex, VALUE))
            _num_hex = input(RIGHTNUMBER)
            continue
        break
    return _num_hex

def get_color_choice(_color_ch):
    while True:
        _color_ch = input(COLOR)
        _color_ch = _color_ch.lower()
        try:
            while _color_ch != 'желтый' and _color_ch != 'красный' and _color_ch != 'синий' and \
                    _color_ch != 'зеленый' and _color_ch != 'оранжевый' and\
                    _color_ch != 'пурпурный' and  _color_ch != 'розовый':
                _color_ch = input(RIGHTCOLOR)
        except ValueError:
            _color_ch = input(RIGHTCOLOR)
            continue
        break
    if _color_ch == 'желтый':
        _color_ch = 'yellow'
    if _color_ch == 'красный':
        _color_ch = 'red'
    if _color_ch == 'синий':
        _color_ch = 'blue'
    if _color_ch == 'зеленый':
        _color_ch = 'green'
    if _color_ch == 'оранжевый':
        _color_ch = 'orange'
    if _color_ch == 'пурпурный':
        _color_ch = 'purple'
    if _color_ch == 'розовый':
        _color_ch = 'pink'
    return _color_ch

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

