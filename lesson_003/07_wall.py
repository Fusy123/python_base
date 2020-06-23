# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код
def briks (start, finish, color, width):
    for x in range (start, finish, 100):
        start_point=sd.get_point(x, y)
        end_point=sd.get_point(x+100, y+50)
        sd.rectangle(start_point, end_point, color=color, width=width)

k=1
for y in range(0, 800, 50):
    if k%2 != 0:
        briks(0, 1200, (255, 240, 125), 2)
    else:
        briks(50, 1200, (125, 240, 125), 2)
    k+=1

# Подсказки:
#  Для отрисовки кирпича использовать функцию rectangle
#  Алгоритм должен получиться приблизительно такой:
#
#   цикл по координате Y
#       вычисляем сдвиг ряда кирпичей
#       цикл координате X
#           вычисляем правый нижний и левый верхний углы кирпича
#           рисуем кирпич

sd.pause()
