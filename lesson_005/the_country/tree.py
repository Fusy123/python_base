import simple_draw as sd


def tree():
    def draw_branches(point1, angle1, length1, delta1, color1):
        if length1 < 5:
            return
        if length1 > 10:
            v1 = sd.get_vector(start_point=point1, angle=angle1, length=length1, width=4)
            v1.draw(color)
            next_point_0 = v1.end_point
            next_angle_0 = angle1 - (sd.random_number(delta1 * .8, delta1 * 1.4))
            next_length_0 = length1 * ((sd.random_number(75 * .8, 75 * 1.2)) / 100)
            draw_branches(next_point_0, next_angle_0, next_length_0, delta1, color1)
            next_angle_0 = angle1 + (sd.random_number(delta1 * .8, delta1 * 1.4))
            next_length_0 = length1 * ((sd.random_number(75 * .8, 75 * 1.2)) / 100)
            draw_branches(next_point_0, next_angle_0, next_length_0, delta1, color1)
        else:
            v1 = sd.get_vector(start_point=point1, angle=angle1, length=length1, width=6)
            v1.draw(color=sd.COLOR_GREEN)
            next_point_0 = v1.end_point
            next_angle_0 = angle1 - (sd.random_number(delta1 * .8, delta1 * 1.4))
            next_length_0 = length1 * ((sd.random_number(75 * .8, 75 * 1.2)) / 100)
            draw_branches(next_point_0, next_angle_0, next_length_0, delta1, color1)
            next_angle_0 = angle1 + (sd.random_number(delta1 * .8, delta1 * 1.4))
            next_length_0 = length1 * ((sd.random_number(75 * .8, 75 * 1.2)) / 100)
            draw_branches(next_point_0, next_angle_0, next_length_0, delta1, color1)

    x = 800
    y = 30
    angle = 90
    length = 100
    delta = 30
    color = (150, 75, 0)
    for i in range(3):
        root_point = sd.get_point(x, y)
        draw_branches(root_point, angle, length, delta, color)
        x += 150
