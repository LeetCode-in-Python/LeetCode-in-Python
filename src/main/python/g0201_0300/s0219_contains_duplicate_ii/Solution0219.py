# #Easy #Array #Hash_Table #Sliding_Window #Top_Interview_150_Hashmap
# #2025_09_14_Time_26_ms_(84.30%)_Space_36.82_MB_(21.63%)

from typing import List, Dict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map_dict = {}
        length = len(nums)
        for i in range(length):
            index = map_dict.get(nums[i])
            if index is not None and abs(index - i) <= k:
                return True
            map_dict[nums[i]] = i
        return False
