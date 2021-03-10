# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

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

    def can_fall(self):
        if self.y < -10:


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

for i in range(N):
    flake = Snowflake(color=color_draw)
    flakes.append(flake)

while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
        flake.can_fall()
        if flake.can_fall():
            flake = Snowflake(color=color_draw)
            flakes.append(flake)
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
