# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd


sd.resolution = (1200, 600)
# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smile(point, step):
    radius = step
    color = sd.random_color()
    sd.circle(center_position=point, radius=radius, color=color, width=0)
    # рисуем глаза
    left_eye = sd.get_point(x - 20, y + 13)
    right_eye = sd.get_point(x + 20, y + 13)
    sd.circle(left_eye, radius=6, color=(0,0,0), width=0)
    sd.circle(right_eye, radius=6, color=(0,0,0), width=0)
    # рисуем нос
    nose_start=sd.get_point(x, y+15)
    nose_finish=sd.get_point(x, y-7)
    sd.line(nose_start, nose_finish, color=(0,0,0), width=2)
    #рисуем рот
    point_list=[sd.get_point(x-28, y-20), sd.get_point(x, y-25), sd.get_point(x+28, y-20)]
    sd.polygon(point_list=point_list, color=(0,0,0), width=0)

for _ in range(10):
    x=sd.random_number(100, 1200)
    y=sd.random_number(100, 600)
    point=sd.get_point(x, y)
    step=sd.random_number(40, 60)
    smile(point=point, step=step)


sd.pause()
