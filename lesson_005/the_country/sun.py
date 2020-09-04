import simple_draw as sd

sunbeam_colors = [sd.COLOR_YELLOW, sd.background_color]

def sun():
    x = 130
    y = 480
    point = sd.get_point(x, y)
    sd.circle(center_position=point, radius=50, color=sd.COLOR_YELLOW, width=0)
    sunbeam = 0
    for color in sunbeam_colors:
        while sunbeam < 361:
            sd.vector(start=point, angle=sunbeam, length=100, color=color, width=3)
            sd.circle(center_position=point, radius=50, color=sd.COLOR_YELLOW, width=0)
            sunbeam += 30
    sd.circle(center_position=point, radius=50, color=sd.background_color, width=5)
    a = sunbeam_colors[0]
    sunbeam_colors.remove(a)
    sunbeam_colors.append(a)
