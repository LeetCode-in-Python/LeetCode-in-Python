# #Easy #String #Programming_Skills_II_Day_6 #Udemy_Arrays #Top_Interview_150_Array/String
# #2025_09_13_Time_0_ms_(100.00%)_Space_12.78_MB_(7.53%)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            if ch == ' ' and length > 0:
                break
            elif ch != ' ':
                length += 1
        return length
