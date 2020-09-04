import simple_draw as sd


def snowflakes():
    N = 50
    snowflake_points = []

    for i in range(N):
        x = sd.random_number(0, 300)
        y = sd.random_number(150, 600)
        length = sd.random_number(10, 40)
        factor_a = (sd.random_number(5, 8)) / 10
        factor_b = (sd.random_number(30, 70)) / 100
        factor_c = sd.random_number(1, 100)
        snowflake_points.append([x, y, length, factor_a, factor_b, factor_c])

    height_snow = 10

    for i in range(N):
        x = snowflake_points[i][0]
        y = snowflake_points[i][1]
        length = snowflake_points[i][2]
        point = sd.get_point(x, y)
        factor_a = snowflake_points[i][3]
        factor_b = snowflake_points[i][4]
        factor_c = snowflake_points[i][5]
        sd.snowflake(point, length, color=sd.background_color, factor_a=factor_a, factor_b=factor_b, factor_c=factor_c)
        y -= sd.random_number(0, 30)
        x += sd.random_number(-15, 15)
        snowflake_points[i] = [x, y, length, factor_a, factor_b, factor_c]
        if y < height_snow:
            snowflake_points[i][1] = sd.random_number(300, 100)
            height_snow += .5
        point = sd.get_point(x, y)
        sd.snowflake(point, length, factor_a=factor_a, factor_b=factor_b, factor_c=factor_c)

