# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

length = 200
width = 5
angle = 0
x = 600
y = 150
point = sd.get_point(x, y)


# пишем функцию рисования фигур
def figure_draw(**kwargs):
    # расчет переменных
    start_point_figure = kwargs['start_point_figure']
    user_angle = kwargs['user_angle']
    angle1 = kwargs['angle']
    length1 = kwargs['length']
    width1 = kwargs['width']
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


def triangle(point1, angle1, length1):
    figure_draw(start_point_figure=point1, angle=angle1, length=length1, width=width, user_angle=3)


def squares(point1, angle1, length1):
    figure_draw(start_point_figure=point1, angle=angle1, length=length1, width=width, user_angle=4)


def pentagon(point1, angle1, length1):
    figure_draw(start_point_figure=point1, angle=angle1, length=length1, width=width, user_angle=5)


def hexagon(point1, angle1, length1):
    figure_draw(start_point_figure=point1, angle=angle1, length=length1, width=width, user_angle=6)


# словарь фигур
figures = ((3, 'Треугольник', triangle), (4, 'Квадрат', squares),
           (5, 'Пятиугольник', pentagon), (6, 'Шестиугольник', hexagon))

# вывод соответствия номеров фигурам
print('Выберите фигуру:  ')

for figure in enumerate(figures):
    print(figure[0], ': ', figure[1][1])

# выбор фигуры и проверка правильности ввода
while True:
    user_figure = int(input('Введите желаемую фигуру: '))
    if 0 <= user_figure <= len(figures) - 1:
        # user_angle = figures[user_figure][0]
        figures[user_figure][2](point, angle, length)
        sd.pause()
        break
    else:
        print('Вы ввели неправильный номер фигуры!')

# зачет!
