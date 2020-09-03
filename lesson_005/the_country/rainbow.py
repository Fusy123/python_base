import simple_draw as sd

def rainbow():
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    point = sd.get_point(600, -60)

    def bubble(point, step):
        radius = 580
        for color in rainbow_colors:
            radius += step
            sd.circle(center_position=point, radius=radius, color=color, width=10)

    bubble(point, 10)
