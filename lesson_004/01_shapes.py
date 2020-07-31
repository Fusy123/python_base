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
# ---------------------------------------------------------------------------------------------------------

# TODO общая функция.
# TODO параметры: количество углов, длина стороны, толщина линии, цвет, стартовая точка,
# TODO расчет наклона в зависимости от количества углов

# TODO Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# TODO Это называется "Выделить общую часть алгоритма в отдельную функцию"
# TODO Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.

# TODO В итоге должно получиться:
# TODO  - одна общая функция со множеством параметров,
# TODO  - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.

# TODO в figure_draw вы вынесете то что часто менялось в коде выше, а потом напишите вот так:

# TODO def triangle(point, angle, length):
# TODO     figure_draw(point, angle, length, и еще нужные параметры для вызова)

# TODO def squares(point, angle, length):
# TODO     figure_draw(point, angle, length, и еще нужные параметры для вызова)

# TODO у вас примерно что то похожее на общею функцию уже реализовано в 03, но нужно доработать

length = 100
width = 3
x = 300
y = 100
angle = 30

# TODO kwargs имелось ввиду именованные параметры которые вы туда передаете
# TODO это: точка рисования, шаг, угол_наклона, длинну линий и все что еще нужно!


def figure_draw(**kwargs):
    color = sd.random_color()
    x1 = x
    y1 = y
    for vertex in range(3, 7, 1):  # расчет переменных
        start_point_figure1 = sd.get_point(x1, y1)
        point1 = start_point_figure1
        angle_start = angle
        angle_step = round(360 / vertex)
        angle_finish = 360 - angle_step

        for angles in range(angle_start, angle_finish, angle_step):  # рисование фигур
            arm = sd.get_vector(start_point=point1, angle=angles, length=length, width=width)
            arm.draw(color=color)
            point1 = arm.end_point
        arm2 = sd.line(start_point=start_point_figure1, end_point=point1, color=color, width=width)
        x1 += 500  # смещение координат для следующей фигуры
        if x1 > 800:
            x1 = 300
            y1 = 300


start_point_figure = sd.get_point(x, y)
figure_draw(angle=angle, length=length, width=width)

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
