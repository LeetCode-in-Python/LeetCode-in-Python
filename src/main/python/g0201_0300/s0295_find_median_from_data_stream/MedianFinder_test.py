import unittest
from MedianFinder import MedianFinder

class MedianFinderTest(unittest.TestCase):
    def test_medianFinder(self):
        median_finder = MedianFinder()
        median_finder.addNum(1)
        median_finder.addNum(2)
        self.assertEqual(median_finder.findMedian(), 1.5)
        median_finder.addNum(3)
        self.assertEqual(median_finder.findMedian(), 2.0)

    def test_medianFinder2(self):
        median_finder = MedianFinder()
        median_finder.addNum(1)
        median_finder.addNum(3)
        median_finder.addNum(-1)
        self.assertEqual(median_finder.findMedian(), 1.0)
