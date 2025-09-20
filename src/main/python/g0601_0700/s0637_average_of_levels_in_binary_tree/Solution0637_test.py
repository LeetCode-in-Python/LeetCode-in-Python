import unittest
from Solution0637 import Solution, TreeNode

class SolutionTest(unittest.TestCase):
    def test_averageOfLevels(self):
        # Tree: [3, 9, 20, null, null, 15, 7]
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        
        result = Solution().averageOfLevels(root)
        expected = [3.00000, 14.50000, 11.00000]
        
        for i in range(len(expected)):
            self.assertAlmostEqual(result[i], expected[i], places=5)

    def test_averageOfLevels2(self):
        # Tree: [3, 9, 20, 15, 7]
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.left.left = TreeNode(15)
        root.left.right = TreeNode(7)
        
        result = Solution().averageOfLevels(root)
        expected = [3.00000, 14.50000, 11.00000]
        
        for i in range(len(expected)):
            self.assertAlmostEqual(result[i], expected[i], places=5)
