import unittest
from geometry.circle import Circle

class TestCircle(unittest.TestCase):
    def test_area(self):
        c = Circle(1)
        self.assertAlmostEqual(c.area(), 3.141592653589793)

    def test_invalid_radius(self):
        with self.assertRaises(ValueError):
            Circle(-1)
