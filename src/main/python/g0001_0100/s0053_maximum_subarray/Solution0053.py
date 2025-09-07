# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #Array #Dynamic_Programming
# #Divide_and_Conquer #Data_Structure_I_Day_1_Array #Dynamic_Programming_I_Day_5
# #Udemy_Famous_Algorithm #Top_Interview_150_Kadane's_Algorithm #Big_O_Time_O(n)_Space_O(1)
# #2025_07_24_Time_50_ms_(77.23%)_Space_32.78_MB_(39.19%)

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float('-inf')
        sum_val = 0
        for num in nums:
            # calculating sub-array sum
            sum_val += num
            maxi = max(sum_val, maxi)
            if sum_val < 0:
                # there is no point to carry a -ve subarray sum. hence setting to 0
                sum_val = 0
        return maxi
