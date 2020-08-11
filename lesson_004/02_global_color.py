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

# TODO добавить доработанный код от 01 урока
# пишем функцию рисования фигур
def figure_draw(**kwargs):
    # расчет переменных
    start_point_figure = kwargs['start_point_figure']
    user_angle = kwargs['user_angle']
    angle1 = kwargs['angle']
    length1 = kwargs['length']
    width1 = kwargs['width']
    color = kwargs['color']
    point2 = start_point_figure
    angle_start = angle1
    angle_step = round(360 / user_angle)
    angle_finish = 361 - angle_step
    for angle_draw in range(angle_start, angle_finish, angle_step):  # рисование фигур
        arm = sd.get_vector(start_point=point2, angle=angle_draw, length=length1, width=width1)
        arm.draw(color=color)
        point2 = arm.end_point
    sd.line(start_point=start_point_figure, end_point=point2, color=color, width=width1)


def triangle(point, angle1, length1):
    figure_draw(start_point_figure=point, angle=angle1, length=length1, width=width, user_angle=3, color=color_draw)


def squares(point, angle1, length1):
    figure_draw(start_point_figure=point, angle=angle1, length=length1, width=width, user_angle=4, color=color_draw)


def pentagon(point, angle1, length1):
    figure_draw(start_point_figure=point, angle=angle1, length=length1, width=width, user_angle=5, color=color_draw)


def hexagon(point, angle1, length1):
    figure_draw(start_point_figure=point, angle=angle1, length=length1, width=width, user_angle=6, color=color_draw)


# словарь цветов
colors = {'1': ['Красный', sd.COLOR_RED],
          '2': ['Оранжевый', sd.COLOR_ORANGE],
          '3': ['Желтый', sd.COLOR_YELLOW],
          '4': ['Зеленый', sd.COLOR_GREEN],
          '5': ['Голубой', sd.COLOR_CYAN],
          '6': ['Синий', sd.COLOR_BLUE],
          '7': ['Фиолетовый', sd.COLOR_PURPLE]
          }

print('Выберите цвет: ')
# вывод соответствия номера - цвету
for color in colors.items():
    print(color[0], ': ', color[1][0])

# выбор цвета и проверка правильности ввода
while True:
    user_color = input('Введите желаемый цвет: ')
    if user_color in colors.keys():
        color_draw = colors[user_color][1]
        break
    else:
        print('Вы ввели неправильный номер цвета!')

angle = 30
length = 100
width = 5
start_point_triangle = sd.get_point(100, 100)
start_point_squares = sd.get_point(600, 100)
start_point_pentagon = sd.get_point(300, 300)
start_point_hexagon = sd.get_point(700, 300)

triangle(start_point_triangle, angle, length)
squares(start_point_squares, angle, length)
pentagon(start_point_pentagon, angle, length)
hexagon(start_point_hexagon, angle, length)

sd.pause()
