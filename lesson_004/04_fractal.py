# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длина ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения
# -------------------------------------------------------------------------------------

root_point = sd.get_point(300, 30)
angle = 90
lehght = 100


def draw_branches(point, angle, length, delta):
    if length < 10:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    # v2 = sd.get_vector(start_point=v1.end_point,angle=angle, length=length, width=3)
    # v2.draw()
    next_point_0 = v1.end_point
    next_point_2 = v1.end_point
    next_angle_0 = angle - delta
    next_angle_2 = angle + delta
    next_length_0 = length * .75
    next_length_2 = length * .75
    draw_branches(point=next_point_0, angle=next_angle_0, length=next_length_0, delta=delta)
    draw_branches(point=next_point_2, angle=next_angle_2, length=next_length_2, delta=delta)

delta = 30
# for delta in range(0, 70, 10):
draw_branches(point=root_point, angle=angle, length=lehght, delta=delta)
# for delta in range(-60, 1, 10):
#      draw_branches(point=root_point, angle=angle, length=lehght, delta=delta1)



# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()
# root_point = sd.get_point(300, 30)
# angle = 90
# lehght = 100
#
#
# def draw_branches(point, angle, length, delta):
#     if length < 10:
#         return
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#     next_point_0 = v1.end_point
#     next_point_2 = v1.end_point
#     next_angle_0 = angle - delta
#     next_angle_2 = angle + delta
#     next_length_0 = length * .75
#     next_length_2 = length * .75
#     draw_branches(point=next_point_0, angle=next_angle_0, length=next_length_0, delta=delta)
#     draw_branches(point=next_point_2, angle=next_angle_2, length=next_length_2, delta=delta)
#
#
# for delta in range(0, 60, 30):
#     draw_branches(point=root_point, angle=angle, length=lehght, delta=delta)

sd.pause()