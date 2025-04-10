# #Medium #Top_100_Liked_Questions #String #Dynamic_Programming
# #Algorithm_II_Day_18_Dynamic_Programming #Dynamic_Programming_I_Day_19
# #Udemy_Dynamic_Programming #Top_Interview_150_Multidimensional_DP #Big_O_Time_O(n^2)_Space_O(n2)
# #2024_06_08_Time_60_ms_(98.17%)_Space_18.5_MB_(81.62%)

class Solution:
    def solve(self, str1, i, str2, j, dp):
        if i==0: return j
        if j==0: return i
        if dp[i][j]!=-1: return dp[i][j]
        if str1[i-1]==str2[j-1]: dp[i][j] = self.solve(str1, i-1, str2, j-1,dp)
        else: dp[i][j] = 1 + min(self.solve(str1, i, str2, j-1,dp),self.solve(str1, i-1, str2, j,dp), self.solve(str1, i-1, str2, j-1,dp))
        return dp[i][j]

    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1), len(word2)
        dp=[[-1]*(n+1) for i in range(m+1)]
        return self.solve(word1, m, word2, n, dp)
