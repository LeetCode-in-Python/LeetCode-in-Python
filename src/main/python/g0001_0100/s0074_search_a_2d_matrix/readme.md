74\. Search a 2D Matrix

Medium

Write an efficient algorithm that searches for a value in an `m x n` matrix. This matrix has the following properties:

*   Integers in each row are sorted from left to right.
*   The first integer of each row is greater than the last integer of the previous row.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/05/mat.jpg)

**Input:** matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3

**Output:** true 

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/10/05/mat2.jpg)

**Input:** matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13

**Output:** false 

**Constraints:**

*   `m == matrix.length`
*   `n == matrix[i].length`
*   `1 <= m, n <= 100`
*   <code>-10<sup>4</sup> <= matrix[i][j], target <= 10<sup>4</sup></code>

To solve this task using Python with a `Solution` class, you can follow these steps:

1. Define a class named `Solution`.
2. Inside the class, define a method named `searchMatrix` that takes `matrix` and `target` as input parameters.
3. Implement the efficient algorithm to search for the target value in the matrix.
4. Use a binary search approach to efficiently find the target value.
5. Start the binary search from the top-right corner of the matrix.
6. If the current element is equal to the target, return True.
7. If the current element is greater than the target, move left in the same row.
8. If the current element is less than the target, move down to the next row.
9. Repeat steps 6-8 until the entire matrix is traversed.
10. If the target is not found, return False.

Here's the implementation:

```python
class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        row, col = 0, cols - 1
        
        while row < rows and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        
        return False

# Example usage:
solution = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(solution.searchMatrix(matrix, 3))   # Output: True
print(solution.searchMatrix(matrix, 13))  # Output: False
```

This solution has a time complexity of O(m + n), where m is the number of rows and n is the number of columns in the matrix. It efficiently searches for the target value by starting the search from the top-right corner and making decisions to move left or down based on the comparison with the current element.