import unittest
from funcs2 import FIFOQueue, LIFOQueue

class TestFuncs2(unittest.TestCase):
    def test_fifo(self):
        q = FIFOQueue()
        self.assertTrue(q.is_empty())
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertFalse(q.is_empty())
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)
        self.assertTrue(q.is_empty())
        with self.assertRaises(IndexError):
            q.dequeue()

    def test_lifo(self):
        s = LIFOQueue()
        self.assertTrue(s.is_empty())
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertFalse(s.is_empty())
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)
        self.assertTrue(s.is_empty())
        with self.assertRaises(IndexError):
            s.pop()

if __name__ == "__main__":
    unittest.main()

