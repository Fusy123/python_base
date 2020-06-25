# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd
sd.resolution = (1200, 600)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

# x=50
# y=50
# x1=1100
# y1=1100
# for lines in rainbow_colors:
#     x+=5
#     x1+=5
#     start_point = sd.get_point(x, 50)
#     end_point = sd.get_point(x1, 450)
#     sd.line(start_point=start_point, end_point=end_point, color=lines, width=4)


# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

point = sd.get_point(600, -60)
def bubble(point, step):
    radius = 380
    for lines in rainbow_colors:
        radius += step
        sd.circle(center_position=point, radius=radius, color=lines, width=40)
bubble(point, 40)
sd.pause()
