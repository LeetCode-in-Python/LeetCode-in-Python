# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #String #Hash_Table
# #Dynamic_Programming #Trie #Memoization #Algorithm_II_Day_15_Dynamic_Programming
# #Dynamic_Programming_I_Day_9 #Udemy_Dynamic_Programming #Big_O_Time_O(M+max*N)_Space_O(M+N+max)
# #2024_06_09_Time_41_ms_(50.55%)_Space_16.6_MB_(88.23%)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [-1] * n

        def solve(i, s):
            if i < 0:
                return True
            if dp[i] != -1:
                return dp[i] == 1
            for w in wordDict:
                sz = len(w)
                if i - sz + 1 >= 0 and s[i - sz + 1 : i + 1] == w:
                    if solve(i - sz, s):
                        dp[i] = 1
                        return True
            dp[i] = 0
            return False

        return solve(n - 1, s)
