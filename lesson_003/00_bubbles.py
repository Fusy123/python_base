# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей

point = sd.get_point(600, 300)
radius = 50

for _ in range(3):
    color = sd.random_color()
    sd.circle(center_position=point, radius=radius, color=color, width=3)
    radius += 5


def bubble(point, step):
    radius = 30
    for _ in range(3):
        color = sd.random_color()
        radius += step
        sd.circle(center_position=point, radius=radius, color=color, width=2)


point = sd.get_point(300, 300)
bubble(point=point, step=10)


# Нарисовать 10 пузырьков в ряд

for x in range(100, 1001, 100):
    point = sd.get_point(x, 300)
    bubble(point=point, step=5)
#
# # Нарисовать три ряда по 10 пузырьков
for y in range(100, 301, 50):
    for x in range(100, 1001, 50):
        point = sd.get_point(x, y)
        bubble(point=point, step=5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

for _ in range(100):
    point = sd.random_point()
    step = random.randint(3, 12)
    bubble(point=point, step=step)

sd.pause()

# зачет!
