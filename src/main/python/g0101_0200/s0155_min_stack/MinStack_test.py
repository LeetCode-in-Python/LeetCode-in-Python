import unittest
from MinStack import MinStack

class MinStackTest(unittest.TestCase):
    def test_minStack(self):
        minStack = MinStack()
        minStack.push(-2)
        minStack.push(0)
        minStack.push(-3)
        self.assertEqual(minStack.getMin(), -3)
        minStack.pop()
        self.assertEqual(minStack.top(), 0)
        self.assertEqual(minStack.getMin(), -2)

    def test_minStack2(self):
        minStack = MinStack()
        minStack.push(0)
        minStack.push(1)
        minStack.push(0)
        self.assertEqual(minStack.getMin(), 0)
        minStack.pop()
        self.assertEqual(minStack.getMin(), 0)

    def test_minStack3(self):
        minStack = MinStack()
        minStack.push(1)
        minStack.push(2)
        self.assertEqual(minStack.top(), 2)
        self.assertEqual(minStack.getMin(), 1)
        minStack.pop()
        self.assertEqual(minStack.getMin(), 1)
        self.assertEqual(minStack.top(), 1)
