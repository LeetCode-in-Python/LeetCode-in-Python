# #Medium #Top_Interview_Questions #String #2024_06_03_Time_29_ms_(95.47%)_Space_16.6_MB_(73.62%)

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
