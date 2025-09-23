# #Medium #Top_100_Liked_Questions #Array #Binary_Search #Matrix #Divide_and_Conquer
# #Data_Structure_II_Day_4_Array #Binary_Search_II_Day_8 #Big_O_Time_O(n+m)_Space_O(1)
# #2025_07_25_Time_143_ms_(64.84%)_Space_24.00_MB_(80.86%)

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        r, c = 0, len(matrix[0]) - 1
        
        while r < len(matrix) and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c -= 1
            else:
                r += 1
        
        return False
