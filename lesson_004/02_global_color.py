# -*- coding: utf-8 -*-
import simple_draw as sd

sd.resolution = (1200, 600)


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


# пишем функцию рисования фигур
def figure_draw(color):
    length = 100
    width = 5
    x = 300
    y = 100
    for vertex in range(3, 7, 1):  # расчет переменных
        start_point_figure = sd.get_point(x, y)
        point = start_point_figure
        angle_start = 30
        angle_step = round(360 / vertex)
        angle_finish = 361 - angle_step

        for angle in range(angle_start, angle_finish, angle_step):  # рисование фигур
            arm = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
            arm.draw(color=color)
            point = arm.end_point
        arm2 = sd.line(start_point=start_point_figure, end_point=point, color=color, width=width)
        x += 500  # смещение координат для следующей фигуры
        if x > 800:
            x = 300
            y = 300


# словарь цветов
colors = {sd.COLOR_RED: ['1', 'Красный'],
          sd.COLOR_ORANGE: ['2', 'Оранжевый'],
          sd.COLOR_YELLOW: ['3', 'Желтый'],
          sd.COLOR_GREEN: ['4', 'Зеленый'],
          sd.COLOR_CYAN: ['5', 'Голубой'],
          sd.COLOR_BLUE: ['6', 'Синий'],
          sd.COLOR_PURPLE: ['7', 'Фиолетовый']
          }

print('Выберите цвет: ')
# вывод соответсвия номера - цвету
for color in colors.items():
    print(color[1][0], ': ', color[1][1])

# выбор цвета и проверка правильности ввода
# TODO используем цикл while True тогда i = 1 не нужно
i = 1
while i == 1:
    user_color = input('Введите желаемый цвет: ')
    # TODO Сразу проверяем вхождение по ключу в условии, и если тру то берем этот ключ и нужные данные
    for color in colors.items():
        if user_color in color[1][0]:
            color_draw = color[0]
            i = 0
            break
    else:
        print('Вы ввели неправильный номер цвета!')
# TODO ругается что данная переменная не объявлена
figure_draw(color=color_draw)
sd.pause()
