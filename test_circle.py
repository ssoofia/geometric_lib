import unittest
import math

from circle import area as circle_area, perimeter as circle_perimeter

class TestCircle(unittest.TestCase):
    
    def test_circle_area_positive(self):
        self.assertEqual(circle_area(5), math.pi * 25)

    def test_circle_area_float(self):
        self.assertEqual(circle_area(2.5), math.pi * 6.25)
    
    def test_circle_perimeter_positive(self):
        self.assertEqual(circle_perimeter(5), 2 * math.pi * 5)

    def test_circle_perimeter_float(self):
        self.assertEqual(circle_perimeter(1.5), 2 * math.pi * 1.5)
        
    def test_circle_area_negative(self):
        self.assertFalse(circle_area(-5))
    
    def test_circle_area_zero(self):
        self.assertFalse(circle_area(0))

    def test_circle_perimeter_negative(self):
        self.assertFalse(circle_perimeter(-5))
    
    def test_circle_perimeter_zero(self):
        self.assertFalse(circle_perimeter(0))
