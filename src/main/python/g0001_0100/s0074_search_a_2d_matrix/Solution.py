# #Medium #Top_100_Liked_Questions #Array #Binary_Search #Matrix #Data_Structure_I_Day_5_Array
# #Algorithm_II_Day_1_Binary_Search #Binary_Search_I_Day_8 #Level_2_Day_8_Binary_Search
# #Udemy_2D_Arrays/Matrix #Big_O_Time_O(endRow+endCol)_Space_O(1)
# #2024_06_09_Time_35_ms_(97.66%)_Space_17_MB_(69.27%)

class Solution:
    def searchMatrix(self, matrix, target):
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

# Example usage:
# sol = Solution()
# matrix = [
#     [1, 3, 5, 7],
#     [10, 11, 16, 20],
#     [23, 30, 34, 60]
# ]
# target = 3
# print(sol.searchMatrix(matrix, target))  # Output should be True
