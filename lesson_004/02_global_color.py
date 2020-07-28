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
colors = (('Красный', sd.COLOR_RED), ('Оранжевый', sd.COLOR_ORANGE), ('Желтый', sd.COLOR_YELLOW),
          ('Зеленый', sd.COLOR_GREEN), ('Голубой', sd.COLOR_CYAN), ('Синий', sd.COLOR_BLUE),
          ('Фиолетовый', sd.COLOR_PURPLE))

print('Выберите цвет: ')
# вывод соответствия номера - цвету
for color in enumerate(colors):
    print(color[0], ': ', color[1][0])

# выбор цвета и проверка правильности ввода
while True:
    user_color = int(input('Введите желаемый цвет: '))
    if 0 <= user_color <= len(colors) - 1:
        color_draw = colors[user_color][1]
        break
    else:
        print('Вы ввели неправильный номер цвета!')

figure_draw(color=color_draw)

sd.pause()
