# #Medium #Top_100_Liked_Questions #Array #Dynamic_Programming #Greedy
# #Algorithm_II_Day_13_Dynamic_Programming #Dynamic_Programming_I_Day_4
# #Big_O_Time_O(n)_Space_O(1) #2024_06_08_Time_89_ms_(99.30%)_Space_17.7_MB_(41.04%)

class Solution:
    def jump(self, nums: List[int]) -> int:
        length = 0
        max_length = 0
        min_jump = 0
        
        for i in range(len(nums) - 1):
            length -= 1
            max_length -= 1
            max_length = max(max_length, nums[i])
            if length <= 0:
                length = max_length
                min_jump += 1
            if length >= len(nums) - i - 1:
                return min_jump
        
        return min_jump
