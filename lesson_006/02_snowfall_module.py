# -*- coding: utf-8 -*-

import simple_draw as sd
import snowfall_engine as se

global snowflake_points
global snowflake_finish

sd.resolution = (1200, 600)


# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# снежинки хранить в глобальных переменных модуля snowfall
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)

N = int(input('Сколько снежинок вы хотите создать? :'))
colors = {'1': ['Красный', sd.COLOR_RED],
          '2': ['Оранжевый', sd.COLOR_ORANGE],
          '3': ['Желтый', sd.COLOR_YELLOW],
          '4': ['Зеленый', sd.COLOR_GREEN],
          '5': ['Белый', sd.COLOR_WHITE],
          '6': ['Темно-Зеленый', sd.COLOR_DARK_GREEN],
          '7': ['Фиолетовый', sd.COLOR_PURPLE]
          }

print('Выберите цвет: ')
# вывод соответствия номера - цвету
for color in colors.items():
    print(color[0], ': ', color[1][0])

# выбор цвета и проверка правильности ввода
while True:
    user_color = input('Введите желаемый цвет: ')
    if se.user_valid_color(user_color, colors) is False:
        print('Вы ввели неправильный номер цвета!')
    else:
        break

se.figure_snowflake(N, se.user_valid_color(user_color, colors))

while True:
    # TODO поробуйте придерживаться данного алгоритма и разбить код в движке на
    # TODO на 5-6 функций описанные ниже.
    # TODO и запустить из в том же порядке.
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    #  сдвинуть_снежинки()
    #  нарисовать_снежинки_цветом(color)
    #  если есть номера_достигших_низа_экрана() то
    #       удалить_снежинки(номера)
    #       создать_снежинки(count)
    # словарь цветов
    sd.start_drawing()
    se.snowflakes_background(N)
    se.snowflakes_drop(N)
    se.snowflakes_color(N)
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
