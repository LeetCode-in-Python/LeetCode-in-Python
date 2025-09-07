# #Easy #Top_100_Liked_Questions #Top_Interview_Questions #Array #Hash_Table #Sorting #Counting
# #Divide_and_Conquer #Data_Structure_II_Day_1_Array #Udemy_Famous_Algorithm
# #Top_Interview_150_Array/String #Big_O_Time_O(n)_Space_O(1)
# #2025_07_25_Time_7_ms_(56.72%)_Space_19.50_MB_(19.10%)

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        majority = nums[0]

        # For Potential Majority Element
        for i in range(1, len(nums)):
            if nums[i] == majority:
                count += 1
            else:
                if count > 1:
                    count -= 1
                else:
                    majority = nums[i]

        # For Confirmation
        count = 0
        for j in nums:
            if j == majority:
                count += 1

        if count >= (len(nums) // 2) + 1:
            return majority
        else:
            return -1
