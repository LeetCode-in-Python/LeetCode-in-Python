# #Easy #Top_100_Liked_Questions #Top_Interview_Questions #Array #Bit_Manipulation
# #LeetCode_75_Bit_Manipulation #Data_Structure_II_Day_1_Array
# #Algorithm_I_Day_14_Bit_Manipulation #Udemy_Integers #Top_Interview_150_Bit_Manipulation
# #Big_O_Time_O(N)_Space_O(1) #2025_07_25_Time_0_ms_(100.00%)_Space_19.69_MB_(43.28%)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res
