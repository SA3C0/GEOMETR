import unittest
from geometry.factory import figure_factory
from geometry.circle import Circle
from geometry.triangle import Triangle

class TestFactory(unittest.TestCase):
    def test_circle_creation(self):
        f = figure_factory('circle', 2)
        self.assertIsInstance(f, Circle)
        self.assertAlmostEqual(f.area(), 3.141592653589793 * 4)

    def test_triangle_creation(self):
        f = figure_factory('triangle', 3, 4, 5)
        self.assertIsInstance(f, Triangle)
        self.assertAlmostEqual(f.area(), 6)

    def test_invalid_shape(self):
        with self.assertRaises(ValueError):
            figure_factory('square', 1, 2, 3, 4)
