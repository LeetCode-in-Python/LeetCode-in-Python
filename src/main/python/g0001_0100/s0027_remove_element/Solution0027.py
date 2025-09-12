# #Easy #Array #Two_Pointers #Top_Interview_150_Array/String
# #2025_09_12_Time_0_ms_(100.00%)_Space_17.75_MB_(52.42%)

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums is None or len(nums) == 0:
            return 0
        length = len(nums)
        j = length - 1
        occur_times = 0
        i = 0
        while i < length:
            if nums[i] == val:
                occur_times += 1
                if j == i:
                    return length - occur_times
                while nums[j] == val:
                    j -= 1
                    occur_times += 1
                    if j == i:
                        return length - occur_times
                nums[i] = nums[j]
                j -= 1
            if i == j:
                return length - occur_times
            i += 1
        return length - occur_times
