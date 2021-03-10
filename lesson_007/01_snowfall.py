# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    # TODO параметр color пересекается с глобальной переменной
    def __init__(self, color=sd.background_color):
        self.count = 0
        self.x = sd.random_number(0, 1200)
        self.y = sd.random_number(450, 600)
        self.length = sd.random_number(10, 40)
        self.factor_a = (sd.random_number(5, 8)) / 10
        self.factor_b = (sd.random_number(30, 70)) / 100
        self.factor_c = sd.random_number(1, 150)
        if color:
            self.color = color

    def move(self):
        # TODO тут у нас должно быть условие используем can_fall если может падать то двигаем
        self.x += sd.random_number(-30, 30)
        self.y -= sd.random_number(5, 50)

    def draw(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length, color=self.color, factor_a=self.factor_a,
                     factor_b=self.factor_b, factor_c=self.factor_c)

    def clear_previous_picture(self, color=sd.background_color):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length, color=color, factor_a=self.factor_a,
                     factor_b=self.factor_b, factor_c=self.factor_c)

    # TODO метод отвечает лишь за то что может ли дальше падать снежинка или нет
    # TODO вот что должно быть return self.y >= -10
    # TODO если снежинка по У больше -10 то может падать
    def can_fall(self):
        numbers_fallen_snowflakes = []  # если потребуется перерисовка сугроба
        if self.y <= -10:
            numbers_fallen_snowflakes.append(self)
        return numbers_fallen_snowflakes




def get_flakes(number):
    # TODO мы должны объявить внутренний список и его вернуть
    # TODO если i в цикле не используется далее нужно ее заменить на _
    for i in range(number):
        # TODO если мы используем в коде color_draw то функция ее должна принять в качестве параметра
        flake = Snowflake(color=color_draw)
        flakes.append(flake)
    return flakes

# TODO еще нужно объявить 2 функции
# get_fallen_flakes
# append_flakes

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
    if user_color in colors.keys():
        color_draw = colors[user_color][1]
        break
    else:
        print('Вы ввели неправильный номер цвета!')

flakes = []
fallen_snow = []
# TODO flakes = get_flakes(count=N)  # создать список снежинок
get_flakes(N)

while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
        fallen_flakes = flake.can_fall()
        if len(fallen_flakes) > 0:
            get_flakes(len(fallen_flakes))
        sd.sleep(0.1)
        if sd.user_want_exit():
            break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()

# TODO оформляем код так чтобы ничего не подчеркивалось и не выделялось по PEP8
