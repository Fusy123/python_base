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
    def draw_triangle(point, angle, length):
        # расчет переменных
        start_point_figure = point
        user_angle = n
        angle1 = angle
        length1 = length
        width1 = 5
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

    return draw_triangle


draw_triangle = get_polygon(n=3)
draw_triangle(point=sd.get_point(600, 100), angle=30, length=150)

sd.pause()
