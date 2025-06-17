# #Medium #Top_100_Liked_Questions #Array #Stack #Monotonic_Stack #LeetCode_75_Monotonic_Stack
# #Programming_Skills_II_Day_6 #Big_O_Time_O(n)_Space_O(n)
# #2024_06_07_Time_864_ms_(87.84%)_Space_30.8_MB_(64.29%)

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
