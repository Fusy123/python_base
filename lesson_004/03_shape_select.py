# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

# пишем функцию рисования фигур
def figure_draw(**kwargs):
    # расчет переменных
    color = sd.random_color()
    point = start_point_figure
    angle_start = 30
    angle_step = round(360 / user_angle)
    angle_finish = 361 - angle_step
    for angle_draw in range(angle_start, angle_finish, angle_step):  # рисование фигур
        arm = sd.get_vector(start_point=point, angle=angle_draw, length=length, width=width)
        arm.draw(color=color)
        point = arm.end_point
    arm2 = sd.line(start_point=start_point_figure, end_point=point, color=color, width=width)


# словарь фигур
figures = ((3, 'Треугольник'), (4, 'Квадрат'), (5, 'Пятиугольник'), (6, 'Шестиугольник'))

# вывод соответствия номеров фигурам
print('Выберите фигуру:  ')

for figure in enumerate(figures):
    print(figure[0], ': ', figure[1][1])


# выбор фигуры и проверка правильности ввода
while True:
    user_figure = int(input('Введите желаемую фигуру: '))
    if 0 <= user_figure <= len(figures) - 1:
        user_angle = figures[user_figure][0]
        break
    else:
        print('Вы ввели неправильный номер фигуры!')


length = 200
width = 5
x = 600
y = 150
start_point_figure = sd.get_point(x, y)


figure_draw(angle=user_angle, start_point=start_point_figure, length=length, width=width)

sd.pause()
