import unittest
from Calculator import Simplecalc


class Testcalc(unittest.TestCase):

    x = Simplecalc()

    def test_add(self):
        self.assertEqual(self.x.add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(self.x.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(self.x.multiply(10, 5), 50)

    def test_divide(self):
        self.assertEqual(self.x.divide(10, 5), 2)


if __name__ == "__main__":
    unittest.main()
