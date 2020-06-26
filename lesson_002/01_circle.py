#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть значение радиуса круга
radius = 42

# Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
# подсказки:
#       формулу можно подсмотреть в интернете,
#       пи возьмите равным 3.1415926
#       точность указывается в функции round()

pi = 3.1415926
s_circle = round(pi * (radius ** 2), 4)

print('Площадь круга: ', s_circle)

# Далее, пусть есть координаты точки
point_1 = (23, 34)

# где 23 - координата х, 34 - координата у

# Если точка point лежит внутри того самого круга [центр в начале координат (0, 0), radius = 42],
# то выведите на консоль True, Или False, если точка лежит вовне круга.
# подсказки:
#       нужно определить расстояние от этой точки до начала координат (0, 0)
#       формула так же есть в интернете
#       квадратный корень - это возведение в степень 0.5
#       операции сравнения дают булевы константы True и False

distance_point_1 = ((0 - point_1[0]) ** 2 + (0 - point_1[1]) ** 2) ** 0.5
print('Расстояние до точки: ', distance_point_1)
# TODO Не непонятно а зачем мы делаем еще одну переменную, с неполной формулой
distance_point_1_1 = (point_1[0] ** 2 + point_1[1] ** 2)
# TODO При сравнении радиус возводить в степень не нужно, сравнивать нужно именно первую переменную с верной формулой
print('Точка входит? ', distance_point_1_1 <= radius ** 2)

# Аналогично для другой точки
point_2 = (30, 30)

# Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True, 30 30
# Или False, если точка лежит вовне круга.

distance_point_2 = ((0 - point_2[0]) ** 2 + (0 - point_2[1]) ** 2) ** 0.5
print('Расстояние до точки: ', distance_point_2)
# TODO Аналогично для с корректировками выше
distance_point_2_1 = (point_2[0] ** 2 + point_2[1] ** 2)
print('Точка входит? ', distance_point_2_1 <= radius ** 2)

# Пример вывода на консоль:
#
# 77777.7777
# False
# False
