# #Medium #Top_100_Liked_Questions #Array #Binary_Search #Matrix #Data_Structure_I_Day_5_Array
# #Algorithm_II_Day_1_Binary_Search #Binary_Search_I_Day_8 #Level_2_Day_8_Binary_Search
# #Udemy_2D_Arrays/Matrix #Top_Interview_150_Binary_Search #Big_O_Time_O(endRow+endCol)_Space_O(1)
# #2025_07_24_Time_0_ms_(100.00%)_Space_18.07_MB_(93.02%)

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        end_row = len(matrix)
        end_col = len(matrix[0])
        target_row = 0
        result = False

        for i in range(end_row):
            if matrix[i][end_col - 1] >= target:
                target_row = i
                break

        for i in range(end_col):
            if matrix[target_row][i] == target:
                result = True
                break

        return result
