# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #String #Dynamic_Programming
# #Data_Structure_II_Day_9_String #Algorithm_II_Day_14_Dynamic_Programming
# #Dynamic_Programming_I_Day_17 #Udemy_Strings #Big_O_Time_O(n)_Space_O(n)
# #2024_06_03_Time_78_ms_(97.43%)_Space_16.7_MB_(47.93%)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Create a new string with separators
        new_str = ['#'] * (2 * len(s) + 1)
        for i in range(len(s)):
            new_str[2 * i + 1] = s[i]

        dp = [0] * len(new_str)
        friend_center = 0
        friend_radius = 0
        lps_center = 0
        lps_radius = 0

        for i in range(len(new_str)):
            if friend_center + friend_radius > i:
                dp[i] = min(dp[2 * friend_center - i], (friend_center + friend_radius) - i)
            else:
                dp[i] = 1

            while i + dp[i] < len(new_str) and i - dp[i] >= 0 and new_str[i + dp[i]] == new_str[i - dp[i]]:
                dp[i] += 1

            if friend_center + friend_radius < i + dp[i]:
                friend_center = i
                friend_radius = dp[i]

            if lps_radius < dp[i]:
                lps_center = i
                lps_radius = dp[i]

        start = (lps_center - lps_radius + 1) // 2
        end = (lps_center + lps_radius - 1) // 2
        return s[start:end]
