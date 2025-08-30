# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #Array #Math #Matrix
# #Data_Structure_II_Day_3_Array #Programming_Skills_II_Day_7 #Udemy_2D_Arrays/Matrix
# #Top_Interview_150_Matrix #Big_O_Time_O(n^2)_Space_O(1)
# #2025_07_24_Time_0_ms_(100.00%)_Space_17.66_MB_(91.44%)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                positions = [
                    [i, j],
                    [j, n - 1 - i],
                    [n - 1 - i, n - 1 - j],
                    [n - 1 - j, i]
                ]
                t = matrix[positions[0][0]][positions[0][1]]
                for k in range(1, len(positions)):
                    temp = matrix[positions[k][0]][positions[k][1]]
                    matrix[positions[k][0]][positions[k][1]] = t
                    t = temp
                matrix[positions[0][0]][positions[0][1]] = t
