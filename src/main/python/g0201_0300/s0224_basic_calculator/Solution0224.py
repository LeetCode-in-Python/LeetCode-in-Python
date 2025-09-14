# #Hard #String #Math #Stack #Recursion #Top_Interview_150_Stack
# #2025_09_14_Time_19_ms_(93.87%)_Space_18.08_MB_(98.80%)

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        num = 0
        sign = 1
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '+':
                result += sign * num
                num = 0
                sign = 1
            elif char == '-':
                result += sign * num
                num = 0
                sign = -1
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
                num = 0
            elif char == ')':
                result += sign * num
                num = 0
                prev_sign = stack.pop()
                prev_result = stack.pop()
                result = prev_result + prev_sign * result
            else:
                continue
        result += sign * num
        return result
