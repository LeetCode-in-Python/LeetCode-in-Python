# #Medium #Top_100_Liked_Questions #Array #Stack #Monotonic_Stack #LeetCode_75_Monotonic_Stack
# #Programming_Skills_II_Day_6 #Big_O_Time_O(n)_Space_O(n)
# #2025_07_25_Time_105_ms_(58.04%)_Space_26.59_MB_(95.95%)

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        sol = [0] * len(temperatures)
        for i in range(len(temperatures) - 2, -1, -1):
            j = i + 1
            while j < len(temperatures):
                if temperatures[i] < temperatures[j]:
                    sol[i] = j - i
                    break
                elif sol[j] == 0:
                    break
                else:
                    j += sol[j]
        return sol
