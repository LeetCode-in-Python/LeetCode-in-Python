# #Medium #Top_100_Liked_Questions #Array #Prefix_Sum #LeetCode_75_Array/String
# #Data_Structure_II_Day_5_Array #Udemy_Arrays #Top_Interview_150_Array/String
# #Big_O_Time_O(n^2)_Space_O(n) #2025_07_25_Time_15_ms_(97.12%)_Space_23.25_MB_(79.77%)

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        ans = [0] * len(nums)
        for num in nums:
            product *= num
        
        for i in range(len(nums)):
            if nums[i] != 0:
                ans[i] = product // nums[i]
            else:
                p = 1
                for j in range(len(nums)):
                    if j != i:
                        p *= nums[j]
                ans[i] = p
                
        return ans
