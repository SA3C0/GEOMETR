import unittest
from geometry.triangle import Triangle

class TestTriangle(unittest.TestCase):
    def test_area(self):
        t = Triangle(3, 4, 5)
        self.assertAlmostEqual(t.area(), 6)

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 10)

    def test_is_right(self):
        t = Triangle(3, 4, 5)
        self.assertTrue(t.is_right())
