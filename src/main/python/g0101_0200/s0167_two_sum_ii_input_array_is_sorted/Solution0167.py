# #Medium #Array #Binary_Search #Two_Pointers #Algorithm_I_Day_3_Two_Pointers
# #Binary_Search_I_Day_7 #Top_Interview_150_Two_Pointers
# #2025_09_14_Time_3_ms_(80.89%)_Space_18.54_MB_(59.40%)

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            sum_val = numbers[i] + numbers[j]
            if sum_val == target:
                return [i + 1, j + 1]
            elif sum_val < target:
                i += 1
            else:
                j -= 1
        return []
