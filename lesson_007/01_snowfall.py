# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку

# класс снежинок
class Snowflake:
    # задаем первоначальные параметры
    def __init__(self, snowcolor=sd.background_color):
        self.x = sd.random_number(0, 1200)
        self.y = sd.random_number(500, 600)
        self.length = sd.random_number(10, 40)
        self.factor_a = (sd.random_number(5, 8)) / 10
        self.factor_b = (sd.random_number(30, 70)) / 100
        self.factor_c = sd.random_number(1, 150)
        if snowcolor:
            self.snowcolor = snowcolor

    # модуль движения снежинок. если в пределах экрана то делаем смещение
    def move(self):
        if self.y >= -(self.length + self.factor_a + self.factor_b + self.factor_c):
            self.x += sd.random_number(-30, 30)
            self.y -= sd.random_number(5, 50)

    # модуль отрисовки снежинки
    def draw(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length, color=self.snowcolor, factor_a=self.factor_a,
                     factor_b=self.factor_b, factor_c=self.factor_c)

    # модуль отрисовки снежинки цветом фона. эффект мультипликации
    def clear_previous_picture(self, snowcolor=sd.background_color):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length, color=snowcolor, factor_a=self.factor_a,
                     factor_b=self.factor_b, factor_c=self.factor_c)


# модуль формирования первоначального списка снежинок
def get_flakes(number, snowcolor):
    snowflakes1 = []
    for _ in range(number):
        snowflake = Snowflake(snowcolor=snowcolor)
        snowflakes1.append(snowflake)
    return snowflakes1


# модуль добавления упавших снежинок в список
def get_fallen_flakes(flakes):
    fallen_snow = []
    for i, flake in enumerate(flakes):
        if flake.y < -40:
            fallen_snow.append(i)
    return fallen_snow


# модуль добавления снежинок
def append_flakes(fallen):
    for _ in range(len(fallen)):
        flake2 = Snowflake(snowcolor=color_draw)
        flakes.append(flake2)
    return flakes


def delete_flakes(numbers):
    numbers.reverse()
    for i in numbers:
        del flakes[i]


# создать_снежинки(N)
N = int(input('Сколько снежинок вы хотите создать? :'))

# список возможных цветов для рисования
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

flakes = get_flakes(number=N, snowcolor=color_draw)
fallen_flakes = []

# основной цикл отрисовки снежинок
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes(flakes)
    if fallen_flakes:
        append_flakes(fallen_flakes)
        delete_flakes(fallen_flakes)
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
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
