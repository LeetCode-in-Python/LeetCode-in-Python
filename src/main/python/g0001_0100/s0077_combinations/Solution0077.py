# #Medium #Backtracking #Algorithm_I_Day_11_Recursion_Backtracking #Top_Interview_150_Backtracking
# #2025_09_13_Time_91_ms_(95.48%)_Space_59.61_MB_(55.55%)

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        # Boundary case
        if n > 20 or k < 1 or k > n:
            return ans
        self._backtrack(ans, n, k, 1, [])
        return ans

    def _backtrack(self, ans: List[List[int]], n: int, k: int, s: int, stack: List[int]):
        # Base case
        # If k becomes 0
        if k == 0:
            ans.append(stack[:])
            return
        # Start with s till n-k+1
        for i in range(s, n - k + 2):
            stack.append(i)
            # Update start for recursion and decrease k by 1
            self._backtrack(ans, n, k - 1, i + 1, stack)
            stack.pop()
