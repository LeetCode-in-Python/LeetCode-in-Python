# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #Array #Matrix #Simulation
# #Programming_Skills_II_Day_8 #Level_2_Day_1_Implementation/Simulation #Udemy_2D_Arrays/Matrix
# #Top_Interview_150_Matrix #2025_09_13_Time_0_ms_(100.00%)_Space_12.44_MB_(54.80%)

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        r = 0
        c = 0
        big_r = len(matrix) - 1
        big_c = len(matrix[0]) - 1
        while r <= big_r and c <= big_c:
            for i in range(c, big_c + 1):
                result.append(matrix[r][i])
            r += 1
            for i in range(r, big_r + 1):
                result.append(matrix[i][big_c])
            big_c -= 1
            if r <= big_r:
                for i in range(big_c, c - 1, -1):
                    result.append(matrix[big_r][i])
                big_r -= 1
            if c <= big_c:
                for i in range(big_r, r - 1, -1):
                    result.append(matrix[i][c])
                c += 1
        return result
