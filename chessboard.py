# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

sd.background_color = sd.COLOR_DARK_ORANGE
sd.resolution = (840, 700)


def cell(x, y):
    cell_point = sd.get_point(x, y)
    sd.square(left_bottom=cell_point, side=side, color=color, width=filling_cell)


def frame():
    sd.square(left_bottom=sd.get_point(x=side * 2, y=side), side=side * 8, color=sd.COLOR_WHITE, width=4)


side = 70
filling_cell = 0
for y in range(side, side * 8 + 1, side):
    for x in range(side * 2, side * 9 + 1, side):
        color = sd.COLOR_DARK_ORANGE if (x + y) % 140 else sd.COLOR_WHITE
        cell(x=x, y=y)
frame()

sd.pause()
