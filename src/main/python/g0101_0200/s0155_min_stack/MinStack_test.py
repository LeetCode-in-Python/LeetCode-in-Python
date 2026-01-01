import unittest
from MinStack import MinStack

class MinStackTest(unittest.TestCase):
    def test_minStack(self):
        min_stack = MinStack()
        min_stack.push(-2)
        min_stack.push(0)
        min_stack.push(-3)
        self.assertEqual(min_stack.getMin(), -3)
        min_stack.pop()
        self.assertEqual(min_stack.top(), 0)
        self.assertEqual(min_stack.getMin(), -2)

    def test_minStack2(self):
        min_stack = MinStack()
        min_stack.push(0)
        min_stack.push(1)
        min_stack.push(0)
        self.assertEqual(min_stack.getMin(), 0)
        min_stack.pop()
        self.assertEqual(min_stack.getMin(), 0)

    def test_minStack3(self):
        min_stack = MinStack()
        min_stack.push(1)
        min_stack.push(2)
        self.assertEqual(min_stack.top(), 2)
        self.assertEqual(min_stack.getMin(), 1)
        min_stack.pop()
        self.assertEqual(min_stack.getMin(), 1)
        self.assertEqual(min_stack.top(), 1)
