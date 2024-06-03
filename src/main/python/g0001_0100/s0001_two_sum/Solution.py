# #Easy #Top_100_Liked_Questions #Top_Interview_Questions #Array #Hash_Table
# #Data_Structure_I_Day_2_Array #Level_1_Day_13_Hashmap #Udemy_Arrays #Big_O_Time_O(n)_Space_O(n)
# #2024_06_03_Time_47_ms_(97.59%)_Space_17.7_MB_(38.78%)

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
