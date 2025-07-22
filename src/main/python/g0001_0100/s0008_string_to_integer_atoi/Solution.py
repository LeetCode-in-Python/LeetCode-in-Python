# #Medium #Top_Interview_Questions #String #Big_O_Time_O(n)_Space_O(n)
# #2025_07_22_Time_0_ms_(100.00%)_Space_17.71_MB_(77.35%)

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if s == '':
            return 0

        result = ''
        i = 0

        negative = False
        if s[0] == '-':
            negative = True
            i += 1
        elif s[0] == '+':
            i += 1

        while i < len(s) and s[i].isnumeric():
            result += s[i]
            i += 1

        if result:
            result = -1*int(result) if negative else int(result)
            if result < -2**31:
                return -2**31
            elif result > 2**31 - 1:
                return 2**31 - 1
            return result
        return 0
