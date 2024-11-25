import unittest
import sys
from triangle import area, perimeter

sys.path.append("..")


class TriangleTestCase(unittest.TestCase):
    def test_zero_sides(self):
        a, b, c = 0, 0, 0
        with self.assertRaises(ValueError):
            area(a, b, c)

        with self.assertRaises(ValueError):
            perimeter(a, b, c)

    def test_positive_sides(self):
        a, b, c = 3, 4, 5
        expected_area = 6
        expected_perimeter = 12

        self.assertAlmostEqual(area(a, b, c), expected_area)
        self.assertEqual(perimeter(a, b, c), expected_perimeter)

    def test_invalid_triangle_inequality(self):
        a, b, c = 1, 2, 10
        with self.assertRaises(ValueError):
            area(a, b, c)

        with self.assertRaises(ValueError):
            perimeter(a, b, c)

    def test_negative_sides(self):
        a, b, c = -3, 4, 5
        with self.assertRaises(ValueError):
            area(a, b, c)

        with self.assertRaises(ValueError):
            perimeter(a, b, c)


if __name__ == "__main__":
    unittest.main()
