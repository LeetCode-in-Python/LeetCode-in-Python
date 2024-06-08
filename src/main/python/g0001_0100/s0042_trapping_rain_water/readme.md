42\. Trapping Rain Water

Hard

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)

**Input:** height = [0,1,0,2,1,0,1,3,2,1,2,1]

**Output:** 6

**Explanation:** The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. 

**Example 2:**

**Input:** height = [4,2,0,3,2,5]

**Output:** 9 

**Constraints:**

*   `n == height.length`
*   <code>1 <= n <= 2 * 10<sup>4</sup></code>
*   <code>0 <= height[i] <= 10<sup>5</sup></code>

To solve the "Trapping Rain Water" problem efficiently, you can use a two-pointer approach. Here are the steps to solve the problem:

### Approach:

1. **Initialize Pointers:**
   - Initialize two pointers `left` and `right` at the two ends of the array `height`.

2. **Initialize Variables:**
   - Initialize variables `max_left` and `max_right` to keep track of the maximum height encountered from the left and right sides, respectively.
   - Initialize a variable `water` to store the total trapped water.

3. **Iterate Through Array:**
   - While `left` pointer is less than `right` pointer, do the following:
     - If `height[left]` is less than or equal to `height[right]`:
       - Update `max_left` to the maximum of `max_left` and `height[left]`.
       - Add `max_left - height[left]` to `water`.
       - Increment `left` pointer.
     - Else:
       - Update `max_right` to the maximum of `max_right` and `height[right]`.
       - Add `max_right - height[right]` to `water`.
       - Decrement `right` pointer.

4. **Return Result:**
   - After the loop ends, return the total trapped water.

### Python Code:

```python
class Solution:
    def trap(self, height):
        n = len(height)
        left, right = 0, n - 1
        max_left = max_right = 0
        water = 0
        
        while left < right:
            if height[left] <= height[right]:
                max_left = max(max_left, height[left])
                water += max_left - height[left]
                left += 1
            else:
                max_right = max(max_right, height[right])
                water += max_right - height[right]
                right -= 1
                
        return water

# Example Usage:
solution = Solution()

# Example 1:
height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
print(solution.trap(height1))  # Output: 6

# Example 2:
height2 = [4,2,0,3,2,5]
print(solution.trap(height2))  # Output: 9
```

This code defines a `Solution` class with a `trap` method to compute how much water can be trapped after raining in the given elevation map represented by the array `height`. The example usage demonstrates how to create an instance of the `Solution` class and call the `trap` method with different inputs.