# #Medium #Top_100_Liked_Questions #Array #Binary_Search #Matrix #Data_Structure_I_Day_5_Array
# #Algorithm_II_Day_1_Binary_Search #Binary_Search_I_Day_8 #Level_2_Day_8_Binary_Search
# #Udemy_2D_Arrays/Matrix #Top_Interview_150_Binary_Search #Big_O_Time_O(endRow+endCol)_Space_O(1)
# #2025_07_24_Time_0_ms_(100.00%)_Space_18.07_MB_(93.02%)

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
