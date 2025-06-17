# #Medium #Top_100_Liked_Questions #String #Stack #Recursion #LeetCode_75_Stack
# #Level_1_Day_14_Stack #Udemy_Strings #Big_O_Time_O(n)_Space_O(n)
# #2024_06_08_Time_28_ms_(91.14%)_Space_16.5_MB_(41.29%)

class Solution:
    def __init__(self):
        self.i = 0

    def decodeString(self, s: str) -> str:
        count = 0
        sb = []
        while self.i < len(s):
            c = s[self.i]
            self.i += 1
            if c.isalpha():
                sb.append(c)
            elif c.isdigit():
                count = count * 10 + int(c)
            elif c == ']':
                break
            elif c == '[':
                # sub problem
                repeat = self.decodeString(s)
                sb.append(repeat * count)
                count = 0
        return ''.join(sb)
