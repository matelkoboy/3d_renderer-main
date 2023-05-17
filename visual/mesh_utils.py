from math import sqrt

def dist_of_points(point_1, point_2):
    dist = sqrt(
        (point_1.x - point_2.x) * (point_1.x - point_2.x) +
        (point_1.y - point_2.y) * (point_1.y - point_2.y) + 
        (point_1.z - point_2.z) * (point_1.z - point_2.z)
    )
    return dist

def closest_point(poly, cam):
    lis = sorted(poly.points, key=lambda mid: dist_of_points(mid, cam))
    return lis[0]

def dist_of_closest_point(poly, point):
    dist = sqrt(
        (closest_point(poly, point).x - point.x) * (closest_point(poly, point).x - point.x) +
        (closest_point(poly, point).y - point.y) * (closest_point(poly, point).y - point.y) + 
        (closest_point(poly, point).z - point.z) * (closest_point(poly, point).z - point.z)
    )
    return dist
    