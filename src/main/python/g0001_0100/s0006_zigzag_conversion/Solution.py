# #Medium #String #2024_06_03_Time_41_ms_(94.82%)_Space_16.5_MB_(92.96%)

class Solution:
        def convert(self, s: str, numRows: int) -> str:
        s_len = len(s)
        if numRows == 1:
        return s

        max_dist = numRows * 2 - 2
        buf = []

        for i in range(numRows):
        index = i
        if i == 0 or i == numRows - 1:
        while index < s_len:
        buf.append(s[index])
        index += max_dist
        else:
        while index < s_len:
        buf.append(s[index])
        index += max_dist - i * 2
        if index >= s_len:
        break
        buf.append(s[index])
        index += i * 2

        return ''.join(buf)
