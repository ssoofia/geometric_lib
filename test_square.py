import unittest

from square import area as square_area, perimeter as square_perimeter

class TestSquare(unittest.TestCase):
    
    def test_square_area_positive(self):
        self.assertEqual(square_area(5), 25)
    
    def test_square_area_float(self):
        self.assertEqual(square_area(3.5), 12.25)
    
    def test_square_perimeter_positive(self):
        self.assertEqual(square_perimeter(5), 20)

    def test_square_perimeter_float(self):
        self.assertEqual(square_perimeter(2.5), 10.0)

    def test_square_area_negative(self):
        self.assertFalse(square_area(-5))
    
    def test_square_area_zero(self):
        self.assertFalse(square_area(0))

    def test_square_perimeter_negative(self):
        self.assertFalse(square_perimeter(-5))
    
    def test_square_perimeter_zero(self):
        self.assertFalse(square_perimeter(0))