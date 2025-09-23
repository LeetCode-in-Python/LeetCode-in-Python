import unittest
from MedianFinder import MedianFinder

class MedianFinderTest(unittest.TestCase):
    def test_medianFinder(self):
        medianFinder = MedianFinder()
        medianFinder.addNum(1)
        medianFinder.addNum(2)
        self.assertEqual(medianFinder.findMedian(), 1.5)
        medianFinder.addNum(3)
        self.assertEqual(medianFinder.findMedian(), 2.0)

    def test_medianFinder2(self):
        medianFinder = MedianFinder()
        medianFinder.addNum(1)
        medianFinder.addNum(3)
        medianFinder.addNum(-1)
        self.assertEqual(medianFinder.findMedian(), 1.0)
