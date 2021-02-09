import simple_draw as sd

snowflakes = []


def user_valid_color(user_color, colors):
    if user_color in colors.keys():
        color_draw = colors[user_color][1]
        return color_draw
    else:
        return False


def create_snowflake(numers):
    global snowflakes
    for _ in range(numers):
        x = sd.random_number(0, 1200)
        y = sd.random_number(150, 600)
        # point = sd.get_point(x, y)
        length = sd.random_number(10, 40)
        factor_a = (sd.random_number(5, 8)) / 10
        # factor_b = (sd.random_number(30, 70)) / 100
        # factor_c = sd.random_number(1, 150)
        snowflakes.append((x, y, length, factor_a))


#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
def draw_snowflake_color(color):
    global snowflakes
    for snowflake in snowflakes:
        point = sd.get_point(snowflake[0], snowflake[1])
        sd.snowflake(center=point, length=snowflake[2], color=color, factor_a=snowflake[3])


#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
def move_snowflakes():
    global snowflakes
    for i, snowflake in enumerate(snowflakes):
        snowflakes[i] = (snowflake[0] + sd.random_number(-30, 30), snowflake[1] - sd.random_number(5, 50))


#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
def numbers_falls():
    global snowflakes
    numbers_fallen_snowflakes = []  # Другая переменная на случай, если потребуется перерисовка сугроба
    for i, snowflake in enumerate(snowflakes):
        if snowflake[1] < 0:
            numbers_fallen_snowflakes.append(i)
    return numbers_fallen_snowflakes


#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
def delete_snowfalls(numbers):
    global snowflakes
    numbers.reverse()
    for i in numbers:
        del snowflakes[i]
