import simple_draw as sd
sd.resolution = (1200, 600)

#рисуем дом с окном, без крыши, раскрашиваем в кирпич

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

#рисуем треугольную крышу дома

def figure_draw(**kwargs):
    # расчет переменных
    start_point_figure = kwargs['start_point_figure']
    user_angle = kwargs['user_angle']
    angle1 = kwargs['angle']
    length1 = kwargs['length']
    width1 = kwargs['width']
    point2 = start_point_figure
    angle_start = angle1
    angle_step = round(360 / user_angle)
    angle_finish = 361 - angle_step
    for angle_draw in range(angle_start, angle_finish, angle_step):  # рисование фигур
        arm = sd.get_vector(start_point=point2, angle=angle_draw, length=length1, width=width1)
        arm.draw(color=sd.COLOR_WHITE)
        point2 = arm.end_point
    sd.line(start_point=start_point_figure, end_point=point2, color=sd.COLOR_WHITE, width=width1)

def triangle(point, angle1, length1):
    figure_draw(start_point_figure=point, angle=angle1, length=length1, width=width, user_angle=3)

angle = 0
length = 350
width = 3
start_point_triangle = sd.get_point(house_x, house_y+350)
triangle(start_point_triangle, angle, length)

sd.pause()