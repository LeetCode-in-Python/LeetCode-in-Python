# #Medium #Top_100_Liked_Questions #Array #Dynamic_Programming #Binary_Search
# #Algorithm_II_Day_16_Dynamic_Programming #Binary_Search_II_Day_3 #Dynamic_Programming_I_Day_18
# #Udemy_Dynamic_Programming #Top_Interview_150_1D_DP #Big_O_Time_O(n*log_n)_Space_O(n)
# #2025_07_25_Time_11_ms_(78.54%)_Space_18.12_MB_(38.75%)

import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        dp = [float('inf')] * (len(nums) + 1)
        dp[0] = float('-inf')  # This makes sure we have a valid comparison at dp[1] = min(dp[1], num)
        
        for num in nums:
            index = bisect.bisect_left(dp, num, 1)  # start searching from index 1
            dp[index] = num
        
        # Find the length of the longest increasing subsequence
        for i in range(len(dp) - 1, 0, -1):
            if dp[i] < float('inf'):
                return i
        return 0
