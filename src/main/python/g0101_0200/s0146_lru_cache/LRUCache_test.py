import unittest
from LRUCache import LRUCache

class SolutionTest(unittest.TestCase):
    def test_lruCache(self):
        lru = LRUCache(2)
        lru.put(1, 1)
        lru.put(2, 2)
        self.assertEqual(lru.get(1), 1)
        lru.put(3, 3)
        self.assertEqual(lru.get(2), -1)
        lru.put(4, 4)
        self.assertEqual(lru.get(1), -1)
        self.assertEqual(lru.get(3), 3)
        self.assertEqual(lru.get(4), 4)

    def test_lruCache2(self):
        lru = LRUCache(1)
        lru.put(2, 1)
        self.assertEqual(lru.get(2), 1)

    def test_lruCache3(self):
        lru = LRUCache(2)
        lru.put(1, 0)
        lru.put(2, 2)
        self.assertEqual(lru.get(1), 0)
        lru.put(3, 3)
        self.assertEqual(lru.get(2), -1)
        lru.put(4, 4)
        self.assertEqual(lru.get(1), -1)
        self.assertEqual(lru.get(3), 3)
        self.assertEqual(lru.get(4), 4)
