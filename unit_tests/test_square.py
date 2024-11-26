import unittest
import sys
from square import area, perimeter

sys.path.append("..")


class SquareAreaTestCase(unittest.TestCase):
    def test_zero_side(self):
        side = 0
        expected_area = 0
        self.assertEqual(area(side), expected_area)

    def test_positive_side(self):
        side = 1
        expected_area = 1
        self.assertEqual(area(side), expected_area)

    def test_negative_side(self):
        side = -1
        with self.assertRaises(ValueError):
            area(side)


class SquarePerimeterTestCase(unittest.TestCase):
    def test_zero_side(self):
        side = 0
        expected_perimeter = 0
        self.assertEqual(perimeter(side), expected_perimeter)

    def test_positive_side(self):
        side = 1
        expected_perimeter = 4
        self.assertEqual(perimeter(side), expected_perimeter)

    def test_negative_side(self):
        side = -1
        with self.assertRaises(ValueError):
            perimeter(side)


if __name__ == "__main__":
    unittest.main()
