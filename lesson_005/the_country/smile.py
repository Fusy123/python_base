import simple_draw as sd

def smile():
    x = 400
    y = 100
    radius = 30
    color = sd.COLOR_YELLOW
    point = sd.get_point(x, y)
    sd.circle(center_position=point, radius=radius, color=color, width=0)
    # рисуем глаза
    left_eye = sd.get_point(x - 10, y + 6)
    right_eye = sd.get_point(x + 10, y + 6)
    sd.circle(left_eye, radius=4, color=sd.COLOR_BLACK, width=0)
    sd.circle(right_eye, radius=4, color=sd.COLOR_BLACK, width=0)
    # рисуем нос
    nose_start = sd.get_point(x, y + 7)
    nose_finish = sd.get_point(x, y - 3)
    sd.line(nose_start, nose_finish, color=sd.COLOR_BLACK, width=2)
    # рисуем рот
    point_list = [sd.get_point(x - 14, y - 10), sd.get_point(x, y - 13), sd.get_point(x + 14, y - 10)]
    sd.polygon(point_list=point_list, color=sd.COLOR_BLACK, width=0)
