import unittest
from electro import calculate_series_resistance, calculate_parallel_resistance


class TestResistances(unittest.TestCase):
    def test_calculate_series_resistance(self):
        self.assertEqual(calculate_series_resistance([10, 20, 30]), 60)
        self.assertEqual(calculate_series_resistance([0, 10, 0]), 10)
        self.assertEqual(calculate_series_resistance([]), 0)

    def test_calculate_parallel_resistance(self):
        self.assertAlmostEqual(calculate_parallel_resistance([10, 20, 30]), 5.45, places=2)
        self.assertEqual(calculate_parallel_resistance([0, 0, 0]), 0)
        self.assertEqual(calculate_parallel_resistance([]), 0)

if __name__ == "__main__":
    unittest.main()


