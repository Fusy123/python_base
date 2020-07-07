# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

sd.resolution = (1200, 600)
sd.background_color = (127, 63, 0)
color = sd.COLOR_WHITE


# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич

def draw_briks(start, finish):
    for x in range(start, finish, 100):
        start_point = sd.get_point(x, y)
        end_point = sd.get_point(x + 100, y + 50)
        sd.rectangle(start_point, end_point, color=color, width=2)


for row, y in enumerate(range(0, 800, 50)):
    if row % 2 != 0:
        draw_briks(0, 1200)
    else:
        draw_briks(50, 1200)

sd.pause()

# зачет!
