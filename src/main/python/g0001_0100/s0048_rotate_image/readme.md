48\. Rotate Image

Medium

You are given an `n x n` 2D `matrix` representing an image, rotate the image by **90** degrees (clockwise).

You have to rotate the image [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm), which means you have to modify the input 2D matrix directly. **DO NOT** allocate another 2D matrix and do the rotation.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg)

**Input:** matrix = [[1,2,3],[4,5,6],[7,8,9]]

**Output:** [[7,4,1],[8,5,2],[9,6,3]] 

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/08/28/mat2.jpg)

**Input:** matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

**Output:** [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]] 

**Example 3:**

**Input:** matrix = [[1]]

**Output:** [[1]] 

**Example 4:**

**Input:** matrix = [[1,2],[3,4]]

**Output:** [[3,1],[4,2]] 

**Constraints:**

*   `matrix.length == n`
*   `matrix[i].length == n`
*   `1 <= n <= 20`
*   `-1000 <= matrix[i][j] <= 1000`

To solve the "Rotate Image" problem, you can perform the rotation in-place by swapping elements of the matrix. Here are the steps to solve the problem:

### Approach:

1. **Transpose the Matrix:**
   - Transpose the matrix by swapping `matrix[i][j]` with `matrix[j][i]` for all `i` and `j` where `i < j`.

2. **Reverse Each Row:**
   - Reverse each row of the transposed matrix to get the final rotated matrix.

### Python Code:

```python
class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        
        # Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reverse each row
        for i in range(n):
            matrix[i] = matrix[i][::-1]

# Example Usage:
solution = Solution()

# Example 1:
matrix1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
solution.rotate(matrix1)
print(matrix1)  # Output: [[7,4,1],[8,5,2],[9,6,3]]

# Example 2:
matrix2 = [
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16]
]
solution.rotate(matrix2)
print(matrix2)  # Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

# Example 3:
matrix3 = [[1]]
solution.rotate(matrix3)
print(matrix3)  # Output: [[1]]

# Example 4:
matrix4 = [
    [1,2],
    [3,4]
]
solution.rotate(matrix4)
print(matrix4)  # Output: [[3,1],[4,2]]
```

This code defines a `Solution` class with a `rotate` method to rotate the given matrix by 90 degrees clockwise. The example usage demonstrates how to create an instance of the `Solution` class and call the `rotate` method with different input matrices.