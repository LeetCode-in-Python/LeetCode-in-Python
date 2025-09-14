# #Medium #String #Two_Pointers #LeetCode_75_Array/String #Udemy_Strings
# #Top_Interview_150_Array/String #2025_09_14_Time_0_ms_(100.00%)_Space_17.89_MB_(69.02%)

class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        i = len(s) - 1
        while i >= 0:
            if s[i] == ' ':
                i -= 1
                continue
            start = s.rfind(' ', 0, i)
            result.append(' ')
            result.append(s[start + 1:i + 1])
            i = start - 1
        if result:
            result.pop(0)  # Remove the leading space
        return ''.join(result)
