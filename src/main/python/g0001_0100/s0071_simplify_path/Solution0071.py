# #Medium #String #Stack #Top_Interview_150_Stack
# #2025_09_13_Time_0_ms_(100.00%)_Space_17.86_MB_(54.70%)

class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split('/')
        stack = []

        for p in parts:
            if(p=='' or p=='.'):
                continue
            elif(p=='..'):
                if stack:
                    stack.pop()
            else:
                stack.append(p)

        return '/'+'/'.join(stack)
