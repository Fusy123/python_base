import simple_draw as sd


def snowflakes():
    N = 50
    snowflake_points = []
    snowflake_finish = []

    for i in range(N):
        x = sd.random_number(0, 600)
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
            snowflake_points[i] = [x, y, length, factor_a, factor_b, factor_c]
            if y < height_snow:
                snowflake_points[i][1] = sd.random_number(500, 600)
                height_snow += .5
            point = sd.get_point(x, y)
            sd.snowflake(point, length, factor_a=factor_a, factor_b=factor_b, factor_c=factor_c)
        sd.finish_drawing()
        sd.sleep(0.1)
        if sd.user_want_exit():
            break
