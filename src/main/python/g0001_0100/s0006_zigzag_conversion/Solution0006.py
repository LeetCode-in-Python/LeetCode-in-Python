# #Medium #String #Top_Interview_150_Array/String #Big_O_Time_O(n)_Space_O(n)
# #2025_07_22_Time_5_ms_(93.09%)_Space_17.85_MB_(70.00%)

class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        s_len = len(s)
        if num_rows == 1:
            return s

        max_dist = num_rows * 2 - 2
        buf = []

        for i in range(num_rows):
            index = i
            if i == 0 or i == num_rows - 1:
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
