# #Medium #Dynamic_Programming #Math #Tree #Binary_Tree #Binary_Search_Tree
# #Dynamic_Programming_I_Day_11 #Big_O_Time_O(n)_Space_O(1)
# #2025_07_24_Time_0_ms_(100.00%)_Space_17.82_MB_(32.26%)

class Solution:
    def numTrees(self, n: int) -> int:
        def factorial(n):
            if n<1: return 1
            return n*factorial(n-1)
        fact = [factorial(i) for i in range(2*n+1)]
        return int(fact[2*n] / (fact[n] * fact[n] * (n+1)))
