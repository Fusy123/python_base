import simple_draw as sd
def sun():
    x = 130
    y = 480
    point = sd.get_point(x, y)
    sd.circle(center_position=point, radius=50, color=sd.COLOR_YELLOW, width=0)
    sunbeam = 0
    while sunbeam < 361:
        sd.vector(start=point, angle=sunbeam, length=100, color=sd.COLOR_YELLOW, width=3)
        sunbeam +=30
    sd.circle(center_position=point, radius=50, color=sd.background_color, width=5)
