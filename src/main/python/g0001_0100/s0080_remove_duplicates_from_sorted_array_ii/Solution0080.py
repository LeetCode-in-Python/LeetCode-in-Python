# #Medium #Array #Two_Pointers #Udemy_Arrays #Top_Interview_150_Array/String
# #2025_09_13_Time_73_ms_(96.40%)_Space_20.27_MB_(96.20%)

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        k = 0
        count = 0
        while i < len(nums) - 1:
            count += 1
            if count <= 2:
                nums[k] = nums[i]
                k += 1
            if nums[i] != nums[i + 1]:
                count = 0
                i += 1
                continue
            i += 1
        count += 1
        if count <= 2:
            nums[k] = nums[i]
            k += 1
        return k
