# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #String #Dynamic_Programming
# #Backtracking #Algorithm_II_Day_11_Recursion_Backtracking #Udemy_Backtracking/Recursion
# #Big_O_Time_O(2^n)_Space_O(n) #2024_06_04_Time_32_ms_(86.75%)_Space_16.8_MB_(83.99%)

class Solution:
    def generateParenthesis(self, n):
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