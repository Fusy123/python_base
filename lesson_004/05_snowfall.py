# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длин лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 50

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

snowflake_points = []
snowflake_finish = []

for i in range(N):
    x = sd.random_number(0, 1200)
    y = sd.random_number(150, 600)
    length = sd.random_number(10, 40)
    factor_a = (sd.random_number(5, 8)) / 10
    factor_b = (sd.random_number(30, 70)) / 100
    factor_c = sd.random_number(1, 150)
    snowflake_points.append([x, y, length, factor_a, factor_b, factor_c])

height_snow = 10

while True:
    sd.start_drawing()
    for i in range(N):
        x = snowflake_points[i][0]
        y = snowflake_points[i][1]
        length = snowflake_points[i][2]
        point = sd.get_point(x, y)
        factor_a = snowflake_points[i][3]
        factor_b = snowflake_points[i][4]
        factor_c = snowflake_points[i][5]
        sd.snowflake(point, length, color=(0, 8, 98), factor_a=factor_a, factor_b=factor_b, factor_c=factor_c)
        y -= sd.random_number(0, 30)
        x += sd.random_number(-15, 15)
        # это мы переместим сюда
        snowflake_points[i] = [x, y, length, factor_a, factor_b, factor_c]
        # а тут мы сделаем вот такую проверку и будет копиться сугроб
        if y < height_snow:
            snowflake_points[i][1] = sd.random_number(500, 600)
            height_snow += .5
        point = sd.get_point(x, y)
        sd.snowflake(point, length, factor_a=factor_a, factor_b=factor_b, factor_c=factor_c)
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# ------------------------------------------------------------------------------------------
# Примерный алгоритм отрисовки снежинок
#   навсегда
#     очистка экрана
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       изменить координата_у и запомнить её в списке по индексу
#       создать точку отрисовки снежинки по координатам
#       нарисовать снежинку белым цветом в этой точке
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл


# Часть 2 (делается после зачета первой части)
#
# Ускорить отрисовку снегопада
# - убрать clear_screen() из цикла: полная очистка всего экрана - долгая операция.
# - использовать хак для стирания старого положения снежинки:
#       отрисуем её заново на старом месте, но цветом фона (sd.background_color) и она исчезнет!
# - использовать функции sd.start_drawing() и sd.finish_drawing()
#       для начала/окончания отрисовки кадра анимации
# - между start_drawing и finish_drawing библиотека sd ничего не выводит на экран,
#       а сохраняет нарисованное в промежуточном буфере, за счет чего достигается ускорение анимации
# - в момент вызова finish_drawing все нарисованное в буфере разом покажется на экране
#
# Примерный алгоритм ускоренной отрисовки снежинок
#   навсегда
#     начать рисование кадра
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       создать точку отрисовки снежинки
#       нарисовать снежинку цветом фона
#       изменить координата_у и запомнить её в списке по индексу
#       создать новую точку отрисовки снежинки
#       нарисовать снежинку на новом месте белым цветом
#     закончить рисование кадра
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл


# Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
