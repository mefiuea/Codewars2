class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y


def find_area(points):
    area = 0
    for idx, point in enumerate(points):
        try:
            x1_temp = points[idx].X
            y1_temp = points[idx].Y
            x2_temp = points[idx + 1].X
            y2_temp = points[idx + 1].Y
        except IndexError:
            break
        area += ((y1_temp + y2_temp) * (x2_temp - x1_temp)) / 2

    return area


print(find_area([Point(0, 0), Point(1, 4), Point(3, 2)]))


# return points[0].X
