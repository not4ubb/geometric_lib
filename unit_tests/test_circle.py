import unittest
import math
import sys
from circle import area, perimeter

sys.path.append("..")


class CircleAreaTestCase(unittest.TestCase):
    def test_zero_radius(self):
        radius = 0
        expected_area = 0
        self.assertEqual(area(radius), expected_area)

    def test_positive_radius(self):
        radius = 1
        expected_area = math.pi
        self.assertEqual(area(radius), expected_area)

    def test_negative_radius(self):
        radius = -1
        with self.assertRaises(ValueError):
            area(radius)

    def test_non_numeric_radius(self):
        radius = "string"
        with self.assertRaises(TypeError):
            area(radius)


class CirclePerimeterTestCase(unittest.TestCase):
    def test_zero_radius(self):
        radius = 0
        expected_perimeter = 0
        self.assertEqual(perimeter(radius), expected_perimeter)

    def test_positive_radius(self):
        radius = 1
        expected_perimeter = 2 * math.pi
        self.assertEqual(perimeter(radius), expected_perimeter)

    def test_negative_radius(self):
        radius = -1
        with self.assertRaises(ValueError):
            perimeter(radius)

    def test_non_numeric_radius(self):
        radius = "string"
        with self.assertRaises(TypeError):
            perimeter(radius)


if __name__ == "__main__":
    unittest.main()
