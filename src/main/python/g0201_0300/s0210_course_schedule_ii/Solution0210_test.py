import unittest
from Solution0210 import Solution

class SolutionTest(unittest.TestCase):
    def test_courseScheduleII(self):
        prerequisites = [[1, 0]]
        num_courses = 2
        self.assertEqual(Solution().findOrder(num_courses, prerequisites), [0, 1])

    def test_courseScheduleII2(self):
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
        num_courses = 4
        self.assertEqual(Solution().findOrder(num_courses, prerequisites), [0, 1, 2, 3])

    def test_courseScheduleII3(self):
        prerequisites = []
        num_courses = 1
        self.assertEqual(Solution().findOrder(num_courses, prerequisites), [0])
