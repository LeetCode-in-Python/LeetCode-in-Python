# #Easy #Top_Interview_Questions #String #Two_Pointers #String_Matching
# #Programming_Skills_II_Day_1 #Top_Interview_150_Array/String
# #2025_09_13_Time_0_ms_(100.00%)_Space_12.36_MB_(81.86%)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        m = len(haystack)
        n = len(needle)
        for start in range(m - n + 1):
            if haystack[start:start + n] == needle:
                return start
        return -1
