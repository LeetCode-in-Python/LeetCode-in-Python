# #Medium #Array #Dynamic_Programming #Divide_and_Conquer #Queue #Monotonic_Queue
# #Dynamic_Programming_I_Day_5 #Top_Interview_150_Kadane's_Algorithm
# #2025_09_20_Time_92_ms_(78.54%)_Space_21.27_MB_(85.27%)

from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def kadane(nums: List[int], sign: int) -> int:
            curr_sum = float('-inf')
            max_sum = float('-inf')
            for num in nums:
                curr_sum = sign * num + max(curr_sum, 0)
                max_sum = max(max_sum, curr_sum)
            return max_sum
        
        sum_of_array = sum(nums)
        max_sum_subarray = kadane(nums, 1)
        min_sum_subarray = kadane(nums, -1) * -1
        
        if sum_of_array == min_sum_subarray:
            return max_sum_subarray
        else:
            return max(max_sum_subarray, sum_of_array - min_sum_subarray)
