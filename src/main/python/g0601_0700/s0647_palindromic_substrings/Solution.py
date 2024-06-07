# #Medium #String #Dynamic_Programming #Big_O_Time_O(n^2)_Space_O(n)
# #2024_06_07_Time_167_ms_(49.16%)_Space_16.4_MB_(97.33%)

class Solution:
    def expand(self, a: List[str], l: int, r: int, res: List[int]) -> None:
        while l >= 0 and r < len(a):
            if a[l] != a[r]:
                return
            else:
                res[0] += 1
                l -= 1
                r += 1

    def countSubstrings(self, s: str) -> int:
        a = list(s)
        res = [0]
        for i in range(len(a)):
            self.expand(a, i, i, res)
            self.expand(a, i, i + 1, res)
        return res[0]
