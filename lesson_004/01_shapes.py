# -*- coding: utf-8 -*-

import simple_draw as sd

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
# start_point_squares = sd.get_point(600, 100)
# start_point_pentagon = sd.get_point(300, 300)
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
# def squares(point, angle, length):
#     arm2 = sd.get_vector(start_point=point, angle=120, length=length, width=3)
#     arm2.draw()
#     for angle in range(30, 271, 90):
#         arm = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#         arm.draw()
#         point = arm.end_point
#
#
# squares(point=start_point_squares, angle=angle, length=length)
#

# ------------------------------------------------------------------------------------------------------
# рисуем пятиугольник
# def pentagon(point, angle, length):
#     arm2 = sd.get_vector(start_point=point, angle=139, length=length, width=3)
#     arm2.draw()
#     for angle in range(30, 289, 72):
#         arm = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#         arm.draw()
#         point = arm.end_point
#
#
# pentagon(point=start_point_pentagon, angle=angle, length=length)
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
# --------------------------------------------------------------------------------------------------------

def figure_draw(**kwargs):
    # расчет переменных
    start_point_figure = kwargs['start_point_figure']
    user_angle = kwargs['user_angle']
    angle1 = kwargs['angle']
    length1 = kwargs['length']
    width1 = kwargs['width']
    color = sd.random_color()
    point2 = start_point_figure
    angle_start = angle1
    angle_step = round(360 / user_angle)
    angle_finish = 361 - angle_step
    for angle_draw in range(angle_start, angle_finish, angle_step):  # рисование фигур
        arm = sd.get_vector(start_point=point2, angle=angle_draw, length=length1, width=width1)
        arm.draw(color=color)
        point2 = arm.end_point
    sd.line(start_point=start_point_figure, end_point=point2, color=color, width=width1)


def triangle(point, angle1, length1):
    figure_draw(start_point_figure=point, angle=angle1, length=length1, width=width, user_angle=3)


def squares(point, angle1, length1):
    figure_draw(start_point_figure=point, angle=angle1, length=length1, width=width, user_angle=4)


def pentagon(point, angle1, length1):
    figure_draw(start_point_figure=point, angle=angle1, length=length1, width=width, user_angle=5)


def hexagon(point, angle1, length1):
    figure_draw(start_point_figure=point, angle=angle1, length=length1, width=width, user_angle=6)


angle = 30
length = 100
width = 5
start_point_triangle = sd.get_point(100, 100)
start_point_squares = sd.get_point(600, 100)
start_point_pentagon = sd.get_point(300, 300)
start_point_hexagon = sd.get_point(700, 300)

triangle(start_point_triangle, angle, length)
squares(start_point_squares, angle, length)
pentagon(start_point_pentagon, angle, length)
hexagon(start_point_hexagon, angle, length)

sd.pause()
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
