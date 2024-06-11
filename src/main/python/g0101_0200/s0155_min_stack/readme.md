155\. Min Stack

Easy

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the `MinStack` class:

*   `MinStack()` initializes the stack object.
*   `void push(int val)` pushes the element `val` onto the stack.
*   `void pop()` removes the element on the top of the stack.
*   `int top()` gets the top element of the stack.
*   `int getMin()` retrieves the minimum element in the stack.

**Example 1:**

**Input**

    ["MinStack","push","push","push","getMin","pop","top","getMin"]
    [[],[-2],[0],[-3],[],[],[],[]]

**Output:** [null,null,null,null,-3,null,0,-2]

**Explanation:**

    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin(); // return -3
    minStack.pop();
    minStack.top(); // return 0
    minStack.getMin(); // return -2 

**Constraints:**

*   <code>-2<sup>31</sup> <= val <= 2<sup>31</sup> - 1</code>
*   Methods `pop`, `top` and `getMin` operations will always be called on **non-empty** stacks.
*   At most <code>3 * 10<sup>4</sup></code> calls will be made to `push`, `pop`, `top`, and `getMin`.

To solve the problem and implement the `MinStack` class that supports `push`, `pop`, `top`, and `getMin` operations in constant time, we can use two stacks:

1. **Main Stack**: This stack stores all the elements.
2. **Min Stack**: This stack keeps track of the minimum elements. Whenever a new element is pushed onto the main stack, it is also pushed onto the min stack if it is less than or equal to the current minimum. When an element is popped from the main stack, it is also popped from the min stack if it is the current minimum.

### Steps:

1. **Initialization**:
   - Create two stacks: `main_stack` and `min_stack`.

2. **Push Operation**:
   - Push the value onto `main_stack`.
   - If `min_stack` is empty or the value is less than or equal to the top of `min_stack`, push the value onto `min_stack`.

3. **Pop Operation**:
   - Pop the value from `main_stack`.
   - If the popped value is equal to the top of `min_stack`, pop it from `min_stack`.

4. **Top Operation**:
   - Return the top value of `main_stack`.

5. **GetMin Operation**:
   - Return the top value of `min_stack`.

### Implementation:

```python
class MinStack:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.main_stack:
            if self.main_stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.main_stack.pop()

    def top(self) -> int:
        if self.main_stack:
            return self.main_stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
```

### Explanation:

1. **Initialization**:
   - The `__init__` method initializes `main_stack` and `min_stack` as empty lists.

2. **Push Operation**:
   - `push(val: int) -> None`: 
     - Adds `val` to `main_stack`.
     - If `min_stack` is empty or `val` is less than or equal to the current minimum (top of `min_stack`), it adds `val` to `min_stack`.

3. **Pop Operation**:
   - `pop() -> None`: 
     - Removes the top element from `main_stack`.
     - If this element is the same as the top element of `min_stack`, it removes the top element from `min_stack` as well.

4. **Top Operation**:
   - `top() -> int`: 
     - Returns the top element of `main_stack`.

5. **GetMin Operation**:
   - `getMin() -> int`: 
     - Returns the top element of `min_stack`, which is the current minimum in the stack.

This implementation ensures that all operations (`push`, `pop`, `top`, and `getMin`) are performed in constant time O(1).