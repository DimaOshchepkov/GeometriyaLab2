import unittest
from Lab2 import is_A_inside_angle_BCD, is_A_inside_polygon

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
if __name__ == '__main__':
    unittest.main()