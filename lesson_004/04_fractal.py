# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)


# sd.background_color = (255, 0, 0)


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

def draw_branches(point1, angle1, length1, delta1, color1):
    if length1 < 10:
        return
    v1 = sd.get_vector(start_point=point1, angle=angle1, length=length1, width=3)
    v1.draw(color)
    next_point_0 = v1.end_point
    next_angle_0 = angle1 - (sd.random_number(delta1 * .8, delta1 * 1.4))
    next_length_0 = length1 * ((sd.random_number(75 * .8, 75 * 1.2)) / 100)
    draw_branches(next_point_0, next_angle_0, next_length_0, delta1, color1)
    next_angle_0 = angle1 + (sd.random_number(delta1 * .8, delta1 * 1.4))
    next_length_0 = length1 * ((sd.random_number(75 * .8, 75 * 1.2)) / 100)
    draw_branches(next_point_0, next_angle_0, next_length_0, delta1, color1)


x = 600
y = 30
root_point = sd.get_point(x, y)
point = root_point
angle = 90
length = 150
delta = 30
color = sd.COLOR_YELLOW
root_point = sd.get_point(x, y)
draw_branches(root_point, angle, length, delta, color)

sd.pause()

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()
