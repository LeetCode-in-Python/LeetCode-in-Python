import unittest
from Solution0173 import BSTIterator, TreeNode

class BSTIteratorTest(unittest.TestCase):
    def test_iteratorBST(self):
        left = TreeNode(3)
        right = TreeNode(15)
        right.left = TreeNode(9)
        right.right = TreeNode(20)
        root = TreeNode(7, left, right)
        iterator = BSTIterator(root)
        self.assertEqual(iterator.next(), 3)
        self.assertEqual(iterator.next(), 7)
        self.assertTrue(iterator.hasNext())
        self.assertEqual(iterator.next(), 9)
        self.assertTrue(iterator.hasNext())
        self.assertEqual(iterator.next(), 15)
        self.assertTrue(iterator.hasNext())
        self.assertEqual(iterator.next(), 20)
        self.assertFalse(iterator.hasNext())
