import math


def calc_angle(point):
    angle_rads = math.atan2(point[1], point[0])  # atan2(y, x)
    angle_degrees = math.degrees(angle_rads)
    print(f"Point ({point[0]}, {point[1]}): {angle_rads} radians or {angle_degrees} degrees")

    # Point in the first quadrant (positive x, positive y)
goalXY = (-64, 60)

calc_angle(goalXY)
calc_angle((0,48))
calc_angle((0,72))
calc_angle((48,0))
