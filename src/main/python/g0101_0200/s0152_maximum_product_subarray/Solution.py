# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #Array #Dynamic_Programming
# #Dynamic_Programming_I_Day_6 #Level_2_Day_13_Dynamic_Programming #Udemy_Dynamic_Programming
# #Big_O_Time_O(N)_Space_O(1) #2024_06_09_Time_71_ms_(61.48%)_Space_17_MB_(43.09%)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = float('-inf')
        cprod = 1

        # Forward pass
        for num in nums:
            cprod *= num
            ans = max(ans, cprod)
            if cprod == 0:
                cprod = 1

        # Backward pass
        cprod = 1
        for num in reversed(nums):
            cprod *= num
            ans = max(ans, cprod)
            if cprod == 0:
                cprod = 1

        return ans
