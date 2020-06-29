# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

sd.resolution = (1200, 600)
sd.background_color = (127, 63, 0)


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

def draw_briks(start, finish, color, width):
    for x in range(start, finish, 100):
        start_point = sd.get_point(x, y)
        end_point = sd.get_point(x + 100, y + 50)
        sd.rectangle(start_point, end_point, color=color, width=width)


# TODO Чтобы в цикле сразу получать номер ряда и Y используйте функцию enumerate(range(0, 800, 50))
# TODO  А если мы Y не используем пишем _, и заводим цикл по количеству рядов range(11)
for y in enumerate(range(0, 800, 50)):
    if y % 2 != 0:
        # TODO Используем константы из библиотеке
        draw_briks(0, 1200, (255, 255, 255), 2)
    else:
        draw_briks(50, 1200, (255, 255, 255), 2)

sd.pause()
