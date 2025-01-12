import unittest
import funcs

class TestFuncs(unittest.TestCase):
    def test_top_three(self):
        self.assertEqual(funcs.top_three([3, 1, 4, 1, 5, 9]), [9, 5, 4])
        self.assertEqual(funcs.top_three([1, 2]), [2, 1])
        self.assertEqual(funcs.top_three([]), [])
    def test_is_prime(self):
        self.assertTrue(funcs.is_prime(2))
        self.assertTrue(funcs.is_prime(13))
        self.assertFalse(funcs.is_prime(4))
        self.assertFalse(funcs.is_prime(1))
        self.assertFalse(funcs.is_prime(-3))
    def test_is_arithmetic_sequence(self):
        self.assertTrue(funcs.is_arithmetic_sequence([1, 3, 5, 7])) 
        self.assertFalse(funcs.is_arithmetic_sequence([1, 2, 4, 8]))  
        self.assertTrue(funcs.is_arithmetic_sequence([10, 10, 10]))  
        self.assertTrue(funcs.is_arithmetic_sequence([])) 
        self.assertTrue(funcs.is_arithmetic_sequence([5])) 

    
