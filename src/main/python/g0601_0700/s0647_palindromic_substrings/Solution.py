# #Medium #String #Dynamic_Programming #Big_O_Time_O(n^2)_Space_O(n)
# #2025_07_25_Time_4_ms_(99.42%)_Space_17.67_MB_(87.53%)

class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        i = 0
        while i < len(s):
            l = i
            while i < len(s) and s[i] == s[l]:
                i+=1
            r = i - 1
            for j in range(r-l+1):
                result += j+1
            while l-1>=0 and r+1 < len(s) and s[l-1] == s[r+1]:
                result+=1

                l-=1
                r+=1
        return result
