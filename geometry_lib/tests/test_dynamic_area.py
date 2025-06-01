import unittest
from geometry.factory import figure_factory

class TestDynamicArea(unittest.TestCase):
    def test_dynamic(self):
        shapes = [
            figure_factory('circle', 1),
            figure_factory('triangle', 3, 4, 5),
        ]
        areas = [shape.area() for shape in shapes]
        self.assertAlmostEqual(areas[0], 3.141592653589793)
        self.assertAlmostEqual(areas[1], 6)
