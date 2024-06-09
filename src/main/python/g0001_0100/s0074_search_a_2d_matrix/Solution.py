# #Medium #Top_100_Liked_Questions #Array #Binary_Search #Matrix #Data_Structure_I_Day_5_Array
# #Algorithm_II_Day_1_Binary_Search #Binary_Search_I_Day_8 #Level_2_Day_8_Binary_Search
# #Udemy_2D_Arrays/Matrix #Big_O_Time_O(endRow+endCol)_Space_O(1)
# #2024_06_09_Time_35_ms_(97.66%)_Space_17_MB_(69.27%)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        endRow = len(matrix)
        endCol = len(matrix[0])
        targetRow = 0
        result = False

        for i in range(endRow):
            if matrix[i][endCol - 1] >= target:
                targetRow = i
                break

        for i in range(endCol):
            if matrix[targetRow][i] == target:
                result = True
                break

        return result
