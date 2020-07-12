# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

# TODO здесь ваш код
# пишем функцию рисования фигур
def figure_draw(angle):
    length = 200
    width = 5
    x = 600
    y = 100
    # расчет переменных
    color = sd.random_color()
    start_point_figure = sd.get_point(x, y)
    point = start_point_figure
    angle_start = 30
    angle_step = round(360 / angle)
    angle_finish = 361 - angle_step
    for angle in range(angle_start, angle_finish, angle_step):  # рисование фигур
        arm = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
        arm.draw(color=color)
        point = arm.end_point
    arm2 = sd.line(start_point=start_point_figure, end_point=point, color=color, width=width)


# словарь фигур
figures = {3: ['1', 'Треугольник'],
           4: ['2', 'Квадрат'],
           5: ['3', 'Пятиугольник'],
           6: ['4', 'Шестиугольник'],
           }

print('Выберите цвет: ')
# вывод соответсвия номера - цвету
for figure in figures.items():
    print(figure[1][0], ': ', figure[1][1])

# выбор цвета и проверка правильности ввода
i = 1
while i == 1:
    user_figure = input('Введите желаемую фигуру: ')
    for figure in figures.items():
        if user_figure in figure[1][0]:
            user_angle = figure[0]
            i = 0
            break
    else:
        print('Вы ввели неправильный номер фигуры!')

figure_draw(angle=user_angle)

sd.pause()
