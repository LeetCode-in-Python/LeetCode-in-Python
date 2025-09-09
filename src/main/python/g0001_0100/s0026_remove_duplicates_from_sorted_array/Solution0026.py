# #Easy #Top_Interview_Questions #Array #Two_Pointers #Top_Interview_150_Array/String

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = 1
        if n <= 1:
            return n
        while j <= n - 1:
            if nums[i] != nums[j]:
                nums[i + 1] = nums[j]
                i += 1
            j += 1
        return i + 1
