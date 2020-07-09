# -*- coding: utf-8 -*-

import simple_draw as sd
from simple_draw import Point

sd.resolution = (1200, 600)


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Примерный алгоритм внутри функции:
#   # будем рисовать с помощью векторов, каждый следующий - из конечной точки предыдущего
#   текущая_точка = начальная точка
#   для угол_наклона из диапазона от 0 до 360 с шагом XXX
#      # XXX подбирается индивидуально для каждой фигуры
#      составляем вектор из текущая_точка заданной длины с наклоном в угол_наклона
#      рисуем вектор
#      текущая_точка = конечной точке вектора
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# ----------------------------------------------------------------------------------------
# рисуем треугольник
# angle = 0
# length = 150
# start_point_triangle = sd.get_point(100, 100)
# TODO  Где именно ошибка? согласно рекомендованного сервиса:
# TODO квадрат сущ. общ.	square; quadrate; regular tetragon; four-square; the second degree;
#  boxball (игра в мяч Lassielle); square of a number (вторая степень числа)
# start_point_quadrate = sd.get_point(600, 100)
# start_point_pentagan = sd.get_point(300, 300)
# start_point_hexagon = sd.get_point(700, 300)


# def triangle(point, angle, length):
#     arm2 = sd.get_vector(start_point=point, angle=90, length=length, width=3)
#     arm2.draw()
#     for angle in range(30, 241, 120):
#         arm = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#         arm.draw()
#         point = arm.end_point
#
#
# triangle(point=start_point_triangle, angle=angle, length=length)
#

# -----------------------------------------------------------------------------------------------------
# рисуем квадрат
# def quadrate(point, angle, length):
#     arm2 = sd.get_vector(start_point=point, angle=120, length=length, width=3)
#     arm2.draw()
#     for angle in range(30, 271, 90):
#         arm = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#         arm.draw()
#         point = arm.end_point
#
#
# quadrate(point=start_point_quadrate, angle=angle, length=length)
#

# ------------------------------------------------------------------------------------------------------
# рисуем пятиугольник
# def pentagan(point, angle, length):
#     arm2 = sd.get_vector(start_point=point, angle=139, length=length, width=3)
#     arm2.draw()
#     for angle in range(30, 289, 72):
#         arm = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#         arm.draw()
#         point = arm.end_point
#
#
# pentagan(point=start_point_pentagan, angle=angle, length=length)
#

# ---------------------------------------------------------------------------------------------------------
# рисуем шестиугольник
# def hexagon(point, angle, length):
#     arm2 = sd.get_vector(start_point=point, angle=150, length=length, width=3)
#     arm2.draw()
#     for angle in range(30, 301, 60):
#         arm = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#         arm.draw()
#         point = arm.end_point
#
#
# hexagon(point=start_point_hexagon, angle=angle, length=length)
# ---------------------------------------------------------------------------------------------------------

# общая функция.
# условие: количество углов, длина стороны, толщина линии, цвет, стартовая точка,
# расчет наклона в зависимости от количества углов

def figure_draw(vertex):
    length = 200
    width = 5
    x = 600
    y = 100
    start_point_figure = sd.get_point(x, y)
    point = start_point_figure
    angle_start = 0
    angle_step = round(360 / vertex)
    angle_finish = 361 - angle_step
    color = sd.random_color()

    for angle in range(angle_start, angle_finish, angle_step):
        arm = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
        arm.draw(color=color)
        point = arm.end_point
    arm2 = sd.line(start_point=start_point_figure, end_point=point, color=color, width=width)


vertex = int(input('Введите количество углов: '))
figure_draw(vertex=vertex)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
