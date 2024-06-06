4\. Median of Two Sorted Arrays

Hard

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median** of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

**Example 1:**

**Input:** nums1 = [1,3], nums2 = [2]

**Output:** 2.00000

**Explanation:** merged array = [1,2,3] and median is 2. 

**Example 2:**

**Input:** nums1 = [1,2], nums2 = [3,4]

**Output:** 2.50000

**Explanation:** merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5. 

**Example 3:**

**Input:** nums1 = [0,0], nums2 = [0,0]

**Output:** 0.00000 

**Example 4:**

**Input:** nums1 = [], nums2 = [1]

**Output:** 1.00000 

**Example 5:**

**Input:** nums1 = [2], nums2 = []

**Output:** 2.00000 

**Constraints:**

*   `nums1.length == m`
*   `nums2.length == n`
*   `0 <= m <= 1000`
*   `0 <= n <= 1000`
*   `1 <= m + n <= 2000`
*   <code>-10<sup>6</sup> <= nums1[i], nums2[i] <= 10<sup>6</sup></code>

Here are the steps to solve the "Median of Two Sorted Arrays" problem:

### Approach:

1. **Combine Arrays:**
   - Combine the two sorted arrays (`nums1` and `nums2`) into a single sorted array (`merged`).
   - This can be done by merging the arrays while maintaining the sorted order.

2. **Find Median:**
   - If the length of the combined array is odd, the median is the middle element.
   - If the length is even, the median is the average of the two middle elements.

3. **Handle Empty Arrays:**
   - If one of the arrays is empty, find the median of the non-empty array.
   - If both arrays are empty, return 0.

### Python Code:

```python
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Combine arrays
        merged = sorted(nums1 + nums2)

        # Find median
        length = len(merged)
        if length % 2 == 1:
            # Odd length
            return float(merged[length // 2])
        else:
            # Even length
            mid1 = merged[length // 2 - 1]
            mid2 = merged[length // 2]
            return (mid1 + mid2) / 2.0

# Example Usage:
solution = Solution()

# Example 1:
nums1_1 = [1, 3]
nums2_1 = [2]
print(solution.findMedianSortedArrays(nums1_1, nums2_1))  # Output: 2.00000

# Example 2:
nums1_2 = [1, 2]
nums2_2 = [3, 4]
print(solution.findMedianSortedArrays(nums1_2, nums2_2))  # Output: 2.50000

# Example 3:
nums1_3 = [0, 0]
nums2_3 = [0, 0]
print(solution.findMedianSortedArrays(nums1_3, nums2_3))  # Output: 0.00000

# Example 4:
nums1_4 = []
nums2_4 = [1]
print(solution.findMedianSortedArrays(nums1_4, nums2_4))  # Output: 1.00000

# Example 5:
nums1_5 = [2]
nums2_5 = []
print(solution.findMedianSortedArrays(nums1_5, nums2_5))  # Output: 2.00000
```

This code defines a `Solution` class with a method `findMedianSortedArrays` that takes two sorted arrays (`nums1` and `nums2`) as input and returns the median of the combined sorted array. The example usage demonstrates how to create an instance of the `Solution` class and call the `findMedianSortedArrays` method with different inputs.