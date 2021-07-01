# -*- coding: utf-8 -*-
import simple_draw as sd

sd.resolution = (1200, 600)


# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    """функция рисования фигур, n - количество переданных вершин"""

    def draw_figure_paint(point, angle, length):
        """подфункция расчета координат вершин фигуры"""
        user_angle = n
        width1 = 5
        color = sd.random_color()
        point2 = point
        angle_start = angle
        angle_step = round(360 / user_angle)
        angle_finish = 361 - angle_step
        for angle_draw in range(angle_start, angle_finish, angle_step):
            arm = sd.get_vector(start_point=point2, angle=angle_draw, length=length, width=width1)
            arm.draw(color=color)
            point2 = arm.end_point
        sd.line(start_point=point, end_point=point2, color=color, width=width1)

    return draw_figure_paint


draw_figure = get_polygon(n=9)
draw_figure(point=sd.get_point(600, 100), angle=30, length=150)

sd.pause()

# зачет!
