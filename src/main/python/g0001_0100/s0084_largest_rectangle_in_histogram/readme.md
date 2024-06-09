84\. Largest Rectangle in Histogram

Hard

Given an array of integers `heights` representing the histogram's bar height where the width of each bar is `1`, return _the area of the largest rectangle in the histogram_.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg)

**Input:** heights = [2,1,5,6,2,3]

**Output:** 10

**Explanation:** The above is a histogram where width of each bar is 1. The largest rectangle is shown in the red area, which has an area = 10 units. 

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/01/04/histogram-1.jpg)

**Input:** heights = [2,4]

**Output:** 4 

**Constraints:**

*   <code>1 <= heights.length <= 10<sup>5</sup></code>
*   <code>0 <= heights[i] <= 10<sup>4</sup></code>

To solve this task using Python with a `Solution` class, you can follow these steps:

1. Define a class named `Solution`.
2. Inside the class, define a method named `largestRectangleArea` that takes `heights` as an input parameter.
3. Implement an algorithm to find the area of the largest rectangle in the histogram.
4. Use a stack-based approach to efficiently find the largest rectangle.
5. Initialize a stack to store the indices of bars in non-decreasing order of heights.
6. Iterate through each bar in the histogram:
    - If the stack is empty or the current bar's height is greater than or equal to the height of the bar at the top of the stack, push the index of the current bar onto the stack.
    - Otherwise, repeatedly pop indices from the stack and calculate the area of the rectangle with the popped bar as the smallest bar. Update the maximum area if necessary.
7. After iterating through all bars, if the stack is not empty, repeat step 6 with remaining bars in the stack.
8. Return the maximum area found.

Here's the implementation:

```python
class Solution:
    def largestRectangleArea(self, heights):
        max_area = 0
        stack = []
        heights.append(0)  # Append 0 to the end to handle the case when all bars are ascending
        
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        
        return max_area

# Example usage:
solution = Solution()
print(solution.largestRectangleArea([2,1,5,6,2,3]))  # Output: 10
print(solution.largestRectangleArea([2,4]))          # Output: 4
```

This solution efficiently finds the largest rectangle area in the histogram using a stack-based approach. It iterates through the histogram only once, resulting in a time complexity of O(n), where n is the number of bars in the histogram.