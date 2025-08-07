# #Easy #Top_100_Liked_Questions #Top_Interview_Questions #String #Stack
# #Data_Structure_I_Day_9_Stack_Queue #Udemy_Strings #Top_Interview_150_Stack
# #Big_O_Time_O(n)_Space_O(n) #2025_07_22_Time_0_ms_(100.00%)_Space_17.79_MB_(80.81%)

class Solution:
    def isValid(self, s: str) -> bool:
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
