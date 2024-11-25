import unittest
from triangle import area, perimeter

class TestTriangle(unittest.TestCase):
    def test_area_valid_triangle(self):
        a, b, c = 3, 4, 5
        expected_area = 6.0
        result = area(a, b, c)
        self.assertAlmostEqual(result, expected_area, places=2)

    def test_perimeter_valid_triangle(self):
        a, b, c = 3, 4, 5
        expected_perimeter = 12
        result = perimeter(a, b, c)
        self.assertEqual(result, expected_perimeter)

    def test_area_invalid_triangle(self):
        with self.assertRaises(ValueError):
            area(1, 2, 10)

    def test_perimeter_invalid_triangle(self):
        with self.assertRaises(ValueError):
            perimeter(1, 2, 10)

    def test_area_negative_sides(self):
        with self.assertRaises(ValueError):
            area(-3, 4, 5)

    def test_perimeter_negative_sides(self):
        with self.assertRaises(ValueError):
            perimeter(-3, 4, 5)

if __name__ == "__main__":
    unittest.main()