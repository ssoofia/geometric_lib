import unittest
import math

from circle import area as circle_area, perimeter as circle_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter

class TestCircle(unittest.TestCase):
    
    def test_circle_area_positive(self):
        self.assertEqual(circle_area(5), math.pi * 25)
    
    def test_circle_area_zero(self):
        self.assertEqual(circle_area(0), 0)
    
    def test_circle_area_float(self):
        self.assertEqual(circle_area(2.5), math.pi * 6.25)
    
    def test_circle_perimeter_positive(self):
        self.assertEqual(circle_perimeter(5), 2 * math.pi * 5)
    
    def test_circle_perimeter_zero(self):
        self.assertEqual(circle_perimeter(0), 0)
    
    def test_circle_perimeter_float(self):
        self.assertEqual(circle_perimeter(1.5), 2 * math.pi * 1.5)

class TestRectangle(unittest.TestCase):
    
    def test_rectangle_area_positive(self):
        self.assertEqual(rectangle_area(5, 10), 50)
    
    def test_rectangle_area_zero_first(self):
        self.assertEqual(rectangle_area(0, 10), 0)
    
    def test_rectangle_area_zero_second(self):
        self.assertEqual(rectangle_area(5, 0), 0)
    
    def test_rectangle_area_both_zero(self):
        self.assertEqual(rectangle_area(0, 0), 0)
    
    def test_rectangle_area_float(self):
        self.assertEqual(rectangle_area(2.5, 4.0), 10.0)
    
    def test_rectangle_perimeter_positive(self):
        self.assertEqual(rectangle_perimeter(5, 10), 30)
    
    def test_rectangle_perimeter_zero_first(self):
        self.assertEqual(rectangle_perimeter(0, 10), 20)
    
    def test_rectangle_perimeter_zero_second(self):
        self.assertEqual(rectangle_perimeter(5, 0), 10)
    
    def test_rectangle_perimeter_both_zero(self):
        self.assertEqual(rectangle_perimeter(0, 0), 0)
    
    def test_rectangle_perimeter_float(self):
        self.assertEqual(rectangle_perimeter(2.5, 3.5), 12.0)

class TestSquare(unittest.TestCase):
    
    def test_square_area_positive(self):
        self.assertEqual(square_area(5), 25)
    
    def test_square_area_zero(self):
        self.assertEqual(square_area(0), 0)
    
    def test_square_area_float(self):
        self.assertEqual(square_area(3.5), 12.25)
    
    def test_square_perimeter_positive(self):
        self.assertEqual(square_perimeter(5), 20)
    
    def test_square_perimeter_zero(self):
        self.assertEqual(square_perimeter(0), 0)
    
    def test_square_perimeter_float(self):
        self.assertEqual(square_perimeter(2.5), 10.0)

class TestTriangle(unittest.TestCase):
    
    def test_triangle_area_positive(self):
        self.assertEqual(triangle_area(10, 5), 25)
    
    def test_triangle_area_zero_base(self):
        self.assertEqual(triangle_area(0, 5), 0)
    
    def test_triangle_area_zero_height(self):
        self.assertEqual(triangle_area(10, 0), 0)
    
    def test_triangle_area_both_zero(self):
        self.assertEqual(triangle_area(0, 0), 0)
    
    def test_triangle_area_float(self):
        self.assertEqual(triangle_area(4.0, 2.5), 5.0)
    
    def test_triangle_perimeter_positive(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)
    
    def test_triangle_perimeter_zero_first(self):
        self.assertEqual(triangle_perimeter(0, 4, 5), 9)
    
    def test_triangle_perimeter_zero_second(self):
        self.assertEqual(triangle_perimeter(3, 0, 5), 8)
    
    def test_triangle_perimeter_zero_third(self):
        self.assertEqual(triangle_perimeter(3, 4, 0), 7)
    
    def test_triangle_perimeter_all_zero(self):
        self.assertEqual(triangle_perimeter(0, 0, 0), 0)
    
    def test_triangle_perimeter_float(self):
        self.assertEqual(triangle_perimeter(1.5, 2.5, 3.0), 7.0)