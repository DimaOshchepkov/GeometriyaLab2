import unittest
from Lab2 import (Point, PolygonInsideManager, is_A_inside_angle_BCD, is_A_inside_polygon,
                  is_simple)

class TestIsPointInsideAngle(unittest.TestCase):
    def test_inside_angle(self):
        A = (1, 1)
        B = (3, 3)
        C = (5, 1)
        D = (3, 0)
        self.assertTrue(is_A_inside_angle_BCD(A, B, C, D))

    def test_inside_angle2(self):
        A = (1, 1)
        B = (3, 3)
        C = (5, 1)
        D = (5, 5)
        self.assertTrue(is_A_inside_angle_BCD(A, B, C, D))
        
    def test_outside_angle(self):
        A = (0, -4)
        B = (3, 3)
        C = (5, 1)
        D = (3, 0)
        self.assertFalse(is_A_inside_angle_BCD(A, B, C, D))
        
    def test_outside_angle2(self):
        A = (5, 5)
        B = (3, 3)
        C = (5, 1)
        D = (10, 5)
        self.assertFalse(is_A_inside_angle_BCD(A, B, C, D))
        
class TestIsAInsidePolygon(unittest.TestCase):

    def test_point_inside_polygon(self):
        polygon = [(0, 0), (0, 4), (4, 4), (4, 0)]
        point_inside = (2, 2)
        self.assertTrue(is_A_inside_polygon(point_inside, polygon))

    def test_point_outside_polygon(self):
        polygon = [(0, 0), (0, 4), (4, 4), (4, 0)]
        point_outside = (5, 5)
        self.assertFalse(is_A_inside_polygon(point_outside, polygon))

    def test_point_on_polygon_edge(self):
        polygon = [(0, 0), (0, 4), (4, 4), (4, 0)]
        point_on_edge = (2, 0)
        self.assertFalse(is_A_inside_polygon(point_on_edge, polygon))

    def test_point_on_polygon_vertex(self):
        polygon = [(0, 0), (0, 4), (4, 4), (4, 0)]
        point_on_vertex = (0, 0)
        self.assertFalse(is_A_inside_polygon(point_on_vertex, polygon))
    
    
    def test_point_on_polygon_edge(self):
        polygon = [(0, 0), (0, 4), (4, 4), (4, 0)]
        point_on_edge = (2, 0)
        self.assertFalse(is_A_inside_polygon(point_on_edge, polygon))

    def test_point_on_polygon_vertex(self):
        polygon = [(0, 0), (0, 4), (4, 4), (4, 0)]
        point_on_vertex = (0, 0)
        self.assertFalse(is_A_inside_polygon(point_on_vertex, polygon))

    def test_fractional_coordinates(self):
        polygon = [(0, 0), (0, 4), (4, 4), (4, 0)]
        point_fractional = (1.5, 1.5)
        self.assertTrue(is_A_inside_polygon(point_fractional, polygon))

    def test_negative_coordinates(self):
        polygon = [(0, 0), (0, 4), (4, 4), (4, 0)]
        point_negative = (-1, -1)
        self.assertFalse(is_A_inside_polygon(point_negative, polygon))


        
class TestSimplePolygon(unittest.TestCase):
    def test_simple_polygon2(self):
        # Тест на простой многоугольник
        Pn_simple = [(-4, 0), (1, 0), (1, 1)]
        self.assertTrue(is_simple(Pn_simple))
        
    def test_simple_polygon(self):
        # Тест на простой многоугольник
        Pn_simple = [(0, 0), (1, 0), (1, 1), (0, 1)]
        self.assertTrue(is_simple(Pn_simple))

    def test_non_simple_polygon(self):
        # Тест на непростой многоугольник (пересечение)
        Pn_non_simple = [(0, 0), (1, 1), (1, 0), (0, 1)]
        self.assertFalse(is_simple(Pn_non_simple))
        
    def test_non_simple_polygon2(self):
        # Тест на не простой многоугольник
        Pn_simple = [(0, 0), (1, 0), (1, 1), (0.75, 0)]
        self.assertFalse(is_simple(Pn_simple))

    def test_empty_polygon(self):
        # Тест на пустой многоугольник
        Pn_empty = []
        self.assertTrue(is_simple(Pn_empty))  # Пустой многоугольник считается простым

    def test_single_point_polygon(self):
        # Тест на многоугольник из одной точки
        Pn_single_point = [(0, 0)]
        self.assertTrue(is_simple(Pn_single_point)) 
        
        
class TestPolygonInsideManager(unittest.TestCase):
    def test_inside_point(self):
        # Тест случая, когда точка находится внутри многоугольника
        polygon = [Point(0, 0), Point(2, 0), Point(2, 2), Point(0, 2)]
        manager = PolygonInsideManager(polygon)
        point_inside = Point(1, 1)
        self.assertTrue(manager.is_inside(point_inside))

    def test_outside_point(self):
        # Тест случая, когда точка находится вне многоугольника
        polygon = [Point(0, 0), Point(2, 0), Point(2, 2), Point(0, 2)]
        manager = PolygonInsideManager(polygon)
        point_outside = Point(3, 3)
        self.assertFalse(manager.is_inside(point_outside))

    def test_on_edge(self):
        # Тест случая, когда точка лежит на грани многоугольника
        polygon = [Point(0, 0), Point(2, 0), Point(2, 2), Point(0, 2)]
        manager = PolygonInsideManager(polygon)
        point_on_edge = Point(1, 2)
        self.assertTrue(manager.is_inside(point_on_edge))
        
    def test_negative_point(self):
        # Тест случая, когда точка находится внутри многоугольника с отрицательными координатами
        polygon = [Point(-2, -2), Point(-2, 2), Point(2, 2), Point(2, -2)]
        manager = PolygonInsideManager(polygon)
        point_inside = Point(-1, -1)
        self.assertTrue(manager.is_inside(point_inside))

    def test_fractional_point(self):
        # Тест случая, когда точка находится внутри многоугольника с дробными координатами
        polygon = [Point(0.5, 0.5), Point(1.5, 0.5), Point(1.5, 1.5), Point(0.5, 1.5)]
        manager = PolygonInsideManager(polygon)
        point_inside = Point(1, 1)
        self.assertTrue(manager.is_inside(point_inside))
        
        
if __name__ == '__main__':
    unittest.main()