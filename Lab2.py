from typing import Tuple, List
import math

def is_A_inside_angle_BCD(A: Tuple[float, float], B: Tuple[float, float], 
                          C: Tuple[float, float], D: Tuple[float, float]) -> bool:
    def arctan2_custom(y, x):
        angle_rad = math.atan2(y, x)
        if angle_rad < 0:
            angle_rad += 2 * math.pi
        return angle_rad
    
    def angel_between(vec_from :Tuple[float, float],
                     vec_to: Tuple[float, float]):
        
        angle_from = arctan2_custom(vec_from[1], vec_from[0])
        angle_to = arctan2_custom(vec_to[1], vec_to[0])
        angle = (angle_to - angle_from) % (2 * math.pi)
        return angle
    
    
    vec_CB = (B[0]- C[0], B[1]-C[1])
    vec_CD = (D[0]- C[0], D[1]-C[1])
    vec_CA = (A[0]- C[0], A[1]-C[1])
    
    BCD = angel_between(vec_CB, vec_CD)
    BCA = angel_between(vec_CB, vec_CA)
    
    return BCA < BCD

# https://www.geeksforgeeks.org/how-to-check-if-a-given-point-lies-inside-a-polygon/
def is_A_inside_polygon(A: Tuple[float, float], polygon: List[Tuple[float, float]]) -> bool:
    num_intersections = 0
    for i in range(len(polygon)):
        p1 = polygon[i]
        p2 = polygon[(i + 1) % len(polygon)]  # Следующая вершина многоугольника (с учетом замыкания)
        if (A[1] > min(p1[1], p2[1]) and A[1] <= max(p1[1], p2[1]) and
            A[0] <= max(p1[0], p2[0]) and p1[1] != p2[1]):
            x_intersection = (A[1] - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1]) + p1[0]
            if p1[0] == p2[0] or A[0] <= x_intersection:
                num_intersections += 1
    return num_intersections % 2 == 1