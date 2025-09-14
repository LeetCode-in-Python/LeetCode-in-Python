# #Medium #Top_Interview_Questions #Array #Math #Stack #Programming_Skills_II_Day_3
# #Top_Interview_150_Stack #2025_09_14_Time_0_ms_(100.00%)_Space_18.88_MB_(99.67%)

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token in {'+', '-', '*', '/'}:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    # Truncate toward zero
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        
        return stack[0]
