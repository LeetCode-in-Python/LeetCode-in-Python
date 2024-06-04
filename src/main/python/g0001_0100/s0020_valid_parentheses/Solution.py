# #Easy #Top_100_Liked_Questions #Top_Interview_Questions #String #Stack
# #Data_Structure_I_Day_9_Stack_Queue #Udemy_Strings #Big_O_Time_O(n)_Space_O(n)
# #2024_06_04_Time_24_ms_(98.16%)_Space_16.5_MB_(67.83%)

class Solution:
    def isValid(self, s):
        stack = []
        for char in s:
            if char in "({[":
                stack.append(char)
            elif char == ')' and stack and stack[-1] == '(':
                stack.pop()
            elif char == '}' and stack and stack[-1] == '{':
                stack.pop()
            elif char == ']' and stack and stack[-1] == '[':
                stack.pop()
            else:
                return False
        return not stack
