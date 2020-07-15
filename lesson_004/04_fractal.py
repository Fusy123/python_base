# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)
sd.background_color = (240, 240, 240)

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
x = 300
y = 30

root_point = sd.get_point(x, y)
angle = 90
lehght = 100
delta = 20


# TODO Пайчарм подчеркивает некоторые параметры потому что они определены выше
def draw_branches(point, angle, length, delta, color):
    if length < 10:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color)
    # TODO дублирование кода, две переменные на один объект
    next_point_0 = v1.end_point
    next_point_2 = v1.end_point
    next_angle_0 = angle - (sd.random_number(delta * .6, delta * 1.4))
    next_angle_2 = angle + (sd.random_number(delta * .6, delta * 1.4))
    next_length_0 = length * ((sd.random_number(75 * .8, 75 * 1.2)) / 100)
    next_length_2 = length * ((sd.random_number(75 * .8, 75 * 1.2)) / 100)
    draw_branches(point=next_point_0, angle=next_angle_0, length=next_length_0, delta=delta, color=color)
    draw_branches(point=next_point_2, angle=next_angle_2, length=next_length_2, delta=delta, color=color)

for _ in range(3):
    color = sd.random_color()
    root_point =sd.get_point (x, y)
    draw_branches(point=root_point, angle=angle, length=lehght, delta=delta, color=color)
    x += 300


sd.pause()

# TODO Есть недочеты в форматировании по PEP8, используйте пункт меню в пайчарме

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()


