import simple_draw as sd

rainbow_colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]

def rainbow():
    point = sd.get_point(500, 80)
    a = rainbow_colors[0]
    rainbow_colors.remove(a)
    rainbow_colors.append(a)
    radius = 730
    for color in rainbow_colors:
        sd.circle(center_position=point, radius=radius, color=color, width=10)
        radius += 10
