import bisect
import functools
import random
from typing import Set, Tuple, List
import math
from typing import NamedTuple

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

def is_A_inside_angle_BCD(A: Tuple[float, float], B: Tuple[float, float], 
                          C: Tuple[float, float], D: Tuple[float, float]) -> bool:
    
    vec_CB = (B[0]- C[0], B[1]-C[1])
    vec_CD = (D[0]- C[0], D[1]-C[1])
    vec_CA = (A[0]- C[0], A[1]-C[1])
    
    BCD = angel_between(vec_CB, vec_CD)
    BCA = angel_between(vec_CB, vec_CA)
    
    return BCA < BCD

# https://www.geeksforgeeks.org/how-to-check-if-a-given-point-lies-inside-a-polygon/
def is_A_inside_polygon(A: Tuple[float, float], polygon: List[Tuple[float, float]]) -> bool:
    """Если провести через точку A какую-нибудь прямую,
    она пересечет стороны многоугольника в четном числе точек.
    При этом на прямой будут чередоваться интервалы, находящиеся
    вне многоугольника и внутри него. Если по обе стороны от точки
    A на прямой окажется четное число точек пересечения со
    сторонами, то точка лежит вне многоугольника, а если нечетное
    – то внутри. 
    Таким образом, алгоритм состоит в следующем:
    выбираем прямую, находим, с какими сторонами она пересекается
    и в каких точках, и считаем количество таких точек с одной
    стороны от A. 
    """
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


# http://e-maxx.ru/algo/segments_intersection_checking
class Point(NamedTuple):
    x: int
    y: int

def area(a: Point, b: Point, c: Point) -> int:
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)

def intersect_1(a: int, b: int, c: int, d: int) -> bool:
    if a > b:
        a, b = b, a
    if c > d:
        c, d = d, c
    return max(a, c) <= min(b, d)

def intersect(a: Point, b: Point, c: Point, d: Point) -> bool:
    return (intersect_1(a.x, b.x, c.x, d.x)
            and intersect_1(a.y, b.y, c.y, d.y)
            and area(a, b, c) * area(a, b, d) <= 0
            and area(c, d, a) * area(c, d, b) <= 0)
    
def is_simple(polygon: List[Tuple[float, float]]):
    n = len(polygon)
    for i in range(n):
        p1 = Point(*polygon[i])
        p2 = Point(*polygon[(i + 1) % n])
        for j in range(i + 2, n-1):
            q1 = Point(*polygon[j])
            q2 = Point(*polygon[(j + 1) % n])
            if intersect(p1, p2, q1, q2):
                return False
    return True


class PolygonInsideManager():
    """1.	Предварительная обработка. 
        Выбрать точку C внутри многоугольника. Для всех лучей с началом в точке C, проходящих через
        вершины многоугольника, вычислить углы, которые они образуют с вертикальным лучом, начинающимся
        в точке C. При этом углы считать “против часовой стрелки”, так что они могут иметь значения
        от 0 до 360 градусов. Теперь каждой вершине многоугольника соответствует число. Поэтому их можно
        занумеровать в порядке возрастания этих чисел: B1B2... BN. На это действие (сортировку) требуется время O(N logN). 
    2.	Ответ на вопрос задачи. 
        Теперь для заданной точки A провести луч CA и вычислить для него угол с вертикальным лучом.
        Теперь надо найти, между какими двумя лучами CBi и CBi+1 проходит луч CA. Это можно сделать
        за время O(log N) – используя бинарный поиск, поскольку лучи расставлены в порядке возрастания
        (или убывания) угла. Теперь осталось только выяснить, лежит ли точка A внутри треугольника CBi_CBi+1. 

    """
    def __midle_point_on_segment(self, segment: Tuple[Point, Point]) -> Point:
        # Выбор случайной точки на отрезке
        p1, p2 = segment
        t = random.uniform(0, 1)
        x = (p1.x + p2.x)/2
        y = (p1.y + p2.y)/2
        return Point(x, y)
    
    def __init__(self, polygon: List[Point]) -> None:
        # Выбор случайного отрезка в многоугольнике
        segment = random.choice([(polygon[i], polygon[(i + 1) % len(polygon)]) for i in range(len(polygon))])
        self.__point_inside = self.__midle_point_on_segment(segment)

        angles: List[self.__RayFromC] = []
        for i in range(len(polygon)):
            vec_from = (0, 1)  # Вектор от вертикальной прямой до точки C
            vec_to = (polygon[i].x - self.__point_inside.x, polygon[i].y - self.__point_inside.y)  # Вектор от C до Bi
            angle = angel_between(vec_from, vec_to)
            angles.append(self.__RayFromC(polygon[i], angle))
        self.__angle = sorted(angles)
        
    def is_inside(self, point: Point) -> bool:
        vec_from = (0, 1)  # Вектор от вертикальной прямой до точки C
        vec_to = (point.x - self.__point_inside.x, point.y - self.__point_inside.y)  # Вектор от C до Bi
        angle = angel_between(vec_from, vec_to)
        
        # Находим индекс первого элемента, большего или равного заданному значению
        index_higher = bisect.bisect_right(self.__angle, self.__RayFromC(vec_to, angle))

        # Находим индекс последнего элемента, меньшего или равного заданному значению
        index_lower = bisect.bisect_left(self.__angle, self.__RayFromC(vec_to, angle)) - 1
        
        # Получаем ближайший элемент больше и меньше заданного значения
        nearest_higher: self.__RayFromC = self.__angle[index_higher % len(self.__angle)]
        nearest_lower: self.__RayFromC = self.__angle[index_lower % len(self.__angle)]

        b1 = nearest_higher.point
        b2 = nearest_lower.point
        
        return is_A_inside_polygon(point, [self.__point_inside, b1, b2])
        
    @functools.total_ordering
    class __RayFromC:
        def __init__(self, point: Point, angle: float):
            self.point = point
            self.angle = angle

        def __eq__(self, other: 'PolygonInsideManager.__RayFromC') -> bool:
            return self.angle == other.angle

        def __lt__(self, other: 'PolygonInsideManager.__RayFromC') -> bool:
            return self.angle < other.angle
        
    