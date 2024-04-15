import unittest
from main import find_maximize_capital

class TestMaximizeCapital(unittest.TestCase):
    def test_basic(self):
        N = 3
        C = 1500
        gains = [200, 300, 400]
        prices = [500, 600, 700]
        self.assertEqual(find_maximize_capital(N, C, gains, prices), 600)

    def test_empty_input(self):
        N = 0
        C = 1000
        gains = []
        prices = []
        self.assertEqual(find_maximize_capital(N, C, gains, prices), 1000)

    def test_insufficient_capital(self):
        N = 3
        C = 200
        gains = [200, 300, 400]
        prices = [500, 600, 700]
        self.assertEqual(find_maximize_capital(N, C, gains, prices), 200)

if __name__ == "__main__":
    unittest.main()
