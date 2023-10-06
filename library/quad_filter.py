def ray_intersects_edge(start, end, point):
    if start[1] > end[1]:
        start, end = end, start
    if point[1] == start[1] or point[1] == end[1]:
        point = (point[0], point[1] + 0.0001)  # Offset the point slightly to avoid corner cases
    if point[1] < start[1] or point[1] > end[1]:
        return False
    if point[0] >= max(start[0], end[0]):
        return False
    if point[0] < min(start[0], end[0]):
        return True
    edge_slope = (end[1] - start[1]) / (end[0] - start[0])
    point_x_intersection = start[0] + (point[1] - start[1]) / edge_slope
    return point[0] < point_x_intersection


def is_inside_quadrilateral(A, B, C, D, P):
    edges = [(A, B), (B, C), (C, D), (D, A)]
    intersections = 0

    for edge in edges:
        if ray_intersects_edge(edge[0], edge[1], P):
            intersections += 1

    return intersections % 2 == 1


def sort_elements(lat0, lat1, lat2, lat3, lat_P, lng0, lng1, lng2, lng3, lng_P):
    A = (float(lat0), float(lng0))
    B = (float(lat1), float(lng1))
    C = (float(lat2), float(lng2))
    D = (float(lat3), float(lng3))
    P = (float(lat_P), float(lng_P))
    if is_inside_quadrilateral(A, B, C, D, P):
        # print("Point P is inside the quadrilateral.")
        return 0
    else:
        return 1
