11\. Container With Most Water

Medium

Given `n` non-negative integers <code>a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub></code> , where each represents a point at coordinate <code>(i, a<sub>i</sub>)</code>. `n` vertical lines are drawn such that the two endpoints of the line `i` is at <code>(i, a<sub>i</sub>)</code> and `(i, 0)`. Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

**Notice** that you may not slant the container.

**Example 1:**

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)

**Input:** height = [1,8,6,2,5,4,8,3,7]

**Output:** 49

**Explanation:** The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49. 

**Example 2:**

**Input:** height = [1,1]

**Output:** 1 

**Example 3:**

**Input:** height = [4,3,2,1,4]

**Output:** 16 

**Example 4:**

**Input:** height = [1,2,1]

**Output:** 2 

**Constraints:**

*   `n == height.length`
*   <code>2 <= n <= 10<sup>5</sup></code>
*   <code>0 <= height[i] <= 10<sup>4</sup></code>

Here are the steps to solve the "Container With Most Water" problem:

### Approach:

1. **Initialize Pointers:**
   - Initialize two pointers, one at the beginning (`left`) and one at the end (`right`) of the height array.

2. **Calculate Initial Area:**
   - Calculate the initial area between the two pointers using the minimum height (`min_height`) and the width (`width`) between the pointers.

3. **Move Pointers Inward:**
   - Move the pointer with the smaller height towards the center of the array.
     - If `height[left] < height[right]`, increment `left`.
     - If `height[left] >= height[right]`, decrement `right`.

4. **Update Maximum Area:**
   - Update the maximum area if the newly calculated area is greater than the current maximum.

5. **Repeat Until Pointers Meet:**
   - Repeat steps 3-4 until the pointers meet.

6. **Return Maximum Area:**
   - Return the maximum area.

### Python Code:

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize pointers
        left, right = 0, len(height) - 1
        max_area = 0

        # Iterate until pointers meet
        while left < right:
            # Calculate width and minimum height
            width = right - left
            min_height = min(height[left], height[right])

            # Update maximum area
            max_area = max(max_area, width * min_height)

            # Move pointers inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        # Return maximum area
        return max_area

# Example Usage:
solution = Solution()

# Example 1:
height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(solution.maxArea(height1))  # Output: 49

# Example 2:
height2 = [1, 1]
print(solution.maxArea(height2))  # Output: 1

# Example 3:
height3 = [4, 3, 2, 1, 4]
print(solution.maxArea(height3))  # Output: 16

# Example 4:
height4 = [1, 2, 1]
print(solution.maxArea(height4))  # Output: 2
```

This code defines a `Solution` class with a method `maxArea` that takes an array of heights as input and returns the maximum area that can be formed by a container. The example usage demonstrates how to create an instance of the `Solution` class and call the `maxArea` method with different inputs.