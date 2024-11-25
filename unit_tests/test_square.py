import unittest
from square import area, perimeter

class TestSquare(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(4), 16)
        self.assertEqual(area(0), 0)

    def test_perimeter(self):
        self.assertEqual(perimeter(4), 16)
        self.assertEqual(perimeter(0), 0)

    def test_negative_side(self):
        with self.assertRaises(ValueError):
            area(-4)
        with self.assertRaises(ValueError):
            perimeter(-4)

if __name__ == "__main__":
    unittest.main()