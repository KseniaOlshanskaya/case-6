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
    _color_ch = input(COLOR)
    _color_ch = _color_ch.lower()
    try:
        while _color_ch != 'yellow' and _color_ch != 'red' and _color_ch != 'blue' and \
                _color_ch != 'green' and _color_ch != 'orange' and\
                _color_ch != 'purple' and  _color_ch != 'pink':
            _color_ch = input(RIGHTCOLOR)
    except ValueError:
        _color_ch = input(RIGHTCOLOR)
    return _color_ch

