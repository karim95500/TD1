import unittest
import funcs

class TestFuncs(unittest.TestCase):
    def test_top_three(self):
        self.assertEqual(funcs.top_three([3, 1, 4, 1, 5, 9]), [9, 5, 4])
        self.assertEqual(funcs.top_three([1, 2]), [2, 1])
        self.assertEqual(funcs.top_three([]), [])
