import simple_draw as sd


def house():
    # рисуем дом с окном, без крыши, раскрашиваем в кирпич
    house_x = 220
    house_y = 10
    ground_start_x = 0
    ground_start_y = 0
    ground_finish_x = 1200
    ground_finish_y = 50

    start_house_point = sd.get_point(house_x, house_y)
    start_ground_point = sd.get_point(ground_start_x, ground_start_y)
    finish_ground_point = sd.get_point(ground_finish_x, ground_finish_y)
    sd.rectangle(start_ground_point, finish_ground_point, sd.COLOR_GREEN, width=0)
    sd.square(left_bottom=start_house_point, side=350, color=sd.COLOR_DARK_ORANGE, width=0)
    sd.square(left_bottom=start_house_point, side=350, color=sd.COLOR_WHITE, width=2)

    def draw_briks(start, finish):
        for x in range(start, finish, 100):
            start_point = sd.get_point(x, y)
            end_point = sd.get_point(x + 50, y + 25)
            sd.rectangle(start_point, end_point, color=sd.COLOR_WHITE, width=2)

    for row, y in enumerate(range(10, 350, 25)):
        if row % 2 != 0:
            draw_briks(220, 570)
        else:
            draw_briks(270, 570)

    window_x = 300
    window_y = 85

    start_window_point = sd.get_point(window_x, window_y)
    sd.square(left_bottom=start_window_point, side=200, color=sd.COLOR_BLUE, width=0)
    sd.square(left_bottom=start_window_point, side=200, color=sd.COLOR_WHITE, width=2)

    # рисуем треугольную крышу дома

    roof_x = 220
    roof_y = 360

    roof_point = (sd.get_point(220, 360), sd.get_point(570, 360), sd.get_point(395, 500))
    sd.polygon(roof_point, color=sd.COLOR_DARK_RED, width=0)
