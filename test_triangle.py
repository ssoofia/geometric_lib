import unittest

from triangle import area as triangle_area, perimeter as triangle_perimeter

class TestTriangle(unittest.TestCase):
    
    def test_triangle_area_positive(self):
        self.assertEqual(triangle_area(10, 5), 25)
    
    def test_triangle_area_float(self):
        self.assertEqual(triangle_area(4.0, 2.5), 5.0)
    
    def test_triangle_perimeter_positive(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)
    
    def test_triangle_perimeter_float(self):
        self.assertEqual(triangle_perimeter(1.5, 2.5, 3.0), 7.0)
        
    def test_triangle_area_negative(self):
        self.assertFalse(triangle_area(-5, 3))
    
    def test_triangle_area_zero(self):
        self.assertFalse(triangle_area(0, 5))

    def test_triangle_perimeter_negative(self):
        self.assertFalse(triangle_perimeter(-3, 4, 5))
        
    def test_triangle_perimeter_bad(self):     
        self.assertFalse(triangle_perimeter(1, 1, 3))
        
    def test_triangle_perimeter_zero(self):
        self.assertFalse(triangle_perimeter(0, 4, 5))