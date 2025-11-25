import unittest

from rectangle import area as rectangle_area, perimeter as rectangle_perimeter

class TestRectangle(unittest.TestCase):
    
    def test_rectangle_area_positive(self):
        self.assertEqual(rectangle_area(5, 10), 50)
    
    def test_rectangle_area_float(self):
        self.assertEqual(rectangle_area(2.5, 4.0), 10.0)
    
    def test_rectangle_perimeter_positive(self):
        self.assertEqual(rectangle_perimeter(5, 10), 30)
    
    def test_rectangle_perimeter_float(self):
        self.assertEqual(rectangle_perimeter(2.5, 3.5), 12.0)
        
    def test_rectangle_area_negative(self):
        self.assertFalse(rectangle_area(-5, 4))
    
    def test_rectangle_area_zero(self):
        self.assertFalse(rectangle_area(0, 5))

    def test_rectangle_perimeter_negative(self):
        self.assertFalse(rectangle_perimeter(-5, 4))
    
    def test_rectangle_perimeter_zero(self):
        self.assertFalse(rectangle_perimeter(0, 5))
