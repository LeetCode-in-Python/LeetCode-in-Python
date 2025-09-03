# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #String #Dynamic_Programming
# #Backtracking #Algorithm_II_Day_11_Recursion_Backtracking #Udemy_Backtracking/Recursion
# #Top_Interview_150_Backtracking #Big_O_Time_O(2^n)_Space_O(n)
# #2025_07_22_Time_0_ms_(100.00%)_Space_18.17_MB_(25.52%)

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self._generate([], ans, n, n)
        return ans

    def _generate(self, current, result, open, close):
        if open == 0 and close == 0:
            result.append("".join(current))
            return
        if open > 0:
            current.append('(')
            self._generate(current, result, open - 1, close)
            current.pop()
        if close > 0 and open < close:
            current.append(')')
            self._generate(current, result, open, close - 1)
            current.pop()
