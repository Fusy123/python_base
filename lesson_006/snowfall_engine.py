import simple_draw as sd


def user_valid_color(user_color, colors):
    if user_color in colors.keys():
        color_draw = colors[user_color][1]
        return color_draw
    else:
        return False


def figure_snowflake(snow, color_draw):
    # TODO если она глобальная ее нужно определить в глобальной области
    global snowflake_points
    snowflake_points = []

    for i in range(snow):
        x = sd.random_number(0, 1200)
        y = sd.random_number(400, 600)
        color = color_draw
        length = sd.random_number(10, 40)
        factor_a = (sd.random_number(5, 8)) / 10
        factor_b = (sd.random_number(30, 40)) / 100
        factor_c = sd.random_number(1, 50)
        snowflake_points.append([x, y, color, length, factor_a, factor_b, factor_c])
    return snowflake_points


def snowflakes(snow):
    # TODO аналогично
    global snowflake_finish
    snowflake_finish = []
    sd.start_drawing()
    for i in range(snow):
        x = snowflake_points[i][0]
        y = snowflake_points[i][1]
        color = snowflake_points[i][2]
        length = snowflake_points[i][3]
        point = sd.get_point(x, y)
        factor_a = snowflake_points[i][4]
        factor_b = snowflake_points[i][5]
        factor_c = snowflake_points[i][6]
        sd.snowflake(point, length, color=sd.background_color, factor_a=factor_a, factor_b=factor_b, factor_c=factor_c)
        y -= sd.random_number(0, 30)
        x += sd.random_number(-15, 15)
        snowflake_points[i] = [x, y, color, length, factor_a, factor_b, factor_c]
        point = sd.get_point(x, y)
        sd.snowflake(point, length, color, factor_a=factor_a, factor_b=factor_b, factor_c=factor_c)
        if y <= -50:
            snowflake_points[i][1] = sd.random_number(400, 600)
        sd.finish_drawing()
