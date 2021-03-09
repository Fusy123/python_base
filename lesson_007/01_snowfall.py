# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self):
        self.x = sd.random_number(0, 1200)
        self.y = sd.random_number(350, 600)
        self.length = sd.random_number(10, 40)
        self.factor_a = (sd.random_number(5, 8)) / 10
        self.factor_b = (sd.random_number(30, 70)) / 100
        self.factor_c = sd.random_number(1, 150)
        self.color = sd.background_color

    def move(self):
        self.x += sd.random_number(-30, 30)
        self.y -= sd.random_number(5, 50)

    def draw(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length, color=sd.COLOR_WHITE, factor_a=self.factor_a,
                     factor_b=self.factor_b, factor_c=self.factor_c)

    def clear_previous_picture(self, color=sd.background_color):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length, color=color, factor_a=self.factor_a,
                     factor_b=self.factor_b, factor_c=self.factor_c)

    def can_fall(self):
        if self.y > -40:
            return True
        else:
            return False


flake = Snowflake()

while True:
    flake.clear_previous_picture()
    flake.move()
    flake.draw()
    if flake.can_fall() == False:
        break
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
