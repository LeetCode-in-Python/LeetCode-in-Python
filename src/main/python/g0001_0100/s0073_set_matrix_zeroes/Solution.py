# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #Array #Hash_Table #Matrix
# #Udemy_2D_Arrays/Matrix #Big_O_Time_O(m*n)_Space_O(1)
# #2024_06_09_Time_93_ms_(94.48%)_Space_17.4_MB_(67.69%)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        row0 = False
        col0 = False

        # Check if 0th column needs to be marked all 0s in future
        for i in range(m):
            if matrix[i][0] == 0:
                col0 = True
                break

        # Check if 0th row needs to be marked all 0s in future
        for j in range(n):
            if matrix[0][j] == 0:
                row0 = True
                break

        # Store the signals in 0th row and column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Mark 0 for all cells based on signal from 0th row and 0th column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Set 0th column
        if col0:
            for i in range(m):
                matrix[i][0] = 0

        # Set 0th row
        if row0:
            for j in range(n):
                matrix[0][j] = 0
