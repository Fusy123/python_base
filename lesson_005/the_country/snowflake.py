import simple_draw as sd

N = 10
snowflake_points = []

for i in range(N):
    x = sd.random_number(0, 200)
    y = sd.random_number(0, 600)
    length = sd.random_number(10, 40)
    factor_a = (sd.random_number(5, 8)) / 10
    factor_b = (sd.random_number(30, 40)) / 100
    factor_c = sd.random_number(1, 50)
    snowflake_points.append([x, y, length, factor_a, factor_b, factor_c])

height_snow = 5


def snowflakes():
    global height_snow

    for i in range(N):
        x = snowflake_points[i][0]
        y = snowflake_points[i][1]
        length = snowflake_points[i][2]
        point = sd.get_point(x, y)
        factor_a = snowflake_points[i][3]
        factor_b = snowflake_points[i][4]
        factor_c = snowflake_points[i][5]
        sd.snowflake(point, length, color=sd.background_color, factor_a=factor_a, factor_b=factor_b, factor_c=factor_c)
        y -= sd.random_number(0, 3)
        x += sd.random_number(-5, 5)
        snowflake_points[i] = [x, y, length, factor_a, factor_b, factor_c]
        if y < height_snow:
            snowflake_points[i][1] = sd.random_number(550, 600)
            height_snow += .5
        point = sd.get_point(x, y)
        sd.snowflake(point, length, factor_a=factor_a, factor_b=factor_b, factor_c=factor_c)

