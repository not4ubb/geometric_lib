import unittest
from calculate import calc

class TestCalculate(unittest.TestCase):
    def test_valid_circle_area(self):
        result = calc("circle", "area", [3])
        self.assertAlmostEqual(result, 28.274333882308138)

    def test_valid_square_perimeter(self):
        result = calc("square", "perimeter", [4])
        self.assertEqual(result, 16)

    def test_invalid_figure(self):
        with self.assertRaises(ValueError):
            calc("triangle", "area", [3, 4, 5])

    def test_invalid_function(self):
        with self.assertRaises(ValueError):
            calc("circle", "volume", [3])

    def test_invalid_size(self):
        with self.assertRaises(TypeError):
            calc("circle", "area", [3, 4])

if __name__ == "__main__":
    unittest.main()