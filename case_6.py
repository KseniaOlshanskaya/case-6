#Ветка Даши (диалог)

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
