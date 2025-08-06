# #Easy #Top_100_Liked_Questions #Top_Interview_Questions #Array #Hash_Table
# #Data_Structure_I_Day_2_Array #Level_1_Day_13_Hashmap #Udemy_Arrays #Top_Interview_150_Hashmap
# #Big_O_Time_O(n)_Space_O(n) #AI_can_be_used_to_solve_the_task
# #2025_07_06_Time_0_ms_(100.00%)_Space_19.05_MB_(23.85%)

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index_map = {}
        for i, num in enumerate(numbers):
            required_num = target - num
            if required_num in index_map:
                return [index_map[required_num], i]
            index_map[num] = i
        return [-1, -1]
