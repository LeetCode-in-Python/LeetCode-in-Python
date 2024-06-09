# #Medium #Dynamic_Programming #Math #Tree #Binary_Tree #Binary_Search_Tree
# #Dynamic_Programming_I_Day_11 #Big_O_Time_O(n)_Space_O(1)
# #2024_06_09_Time_30_ms_(84.13%)_Space_16.4_MB_(71.22%)

class Solution:
    def numTrees(self, n: int) -> int:
        def factorial(n):
            if n<1: return 1
            return n*factorial(n-1)
        fact = [factorial(i) for i in range(2*n+1)]
        return int(fact[2*n] / (fact[n] * fact[n] * (n+1)))
