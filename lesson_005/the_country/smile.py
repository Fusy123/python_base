import simple_draw as sd
x = 400
y = 180
radius = 50
color = [sd.COLOR_YELLOW, sd.COLOR_BLACK]
glosso_color = [sd.COLOR_RED, sd.COLOR_YELLOW]
point = sd.get_point(x, y)


def smile():
    sd.circle(center_position=point, radius=radius, color=sd.COLOR_YELLOW, width=0)
    # рисуем глаза
    left_eye = sd.get_point(x - 20, y + 12)
    right_eye = sd.get_point(x + 20, y + 12)
    for colors in color:
        sd.circle(left_eye, radius=4, color=colors, width=0)
        sd.circle(right_eye, radius=4, color=colors, width=0)
    a = color[0]
    color.remove(a)
    color.append(a)

    # рисуем нос
    nose_start = sd.get_point(x, y + 10)
    nose_finish = sd.get_point(x, y - 10)
    sd.line(nose_start, nose_finish, color=sd.COLOR_BLACK, width=2)
    # рисуем рот
    point_list = [sd.get_point(x - 24, y - 30), sd.get_point(x, y - 20), sd.get_point(x + 24, y - 30)]
    sd.polygon(point_list=point_list, color=sd.COLOR_BLACK, width=0)
    glosso_point = sd.get_point(x, y - 35)
    for glcolors in glosso_color:
        sd.circle(glosso_point, radius=5, color=glcolors, width=0)
    b = glosso_color[0]
    glosso_color.remove(b)
    glosso_color.append(b)



