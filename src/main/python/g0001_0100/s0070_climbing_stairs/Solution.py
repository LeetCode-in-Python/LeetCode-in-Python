# #Easy #Top_100_Liked_Questions #Top_Interview_Questions #Dynamic_Programming #Math #Memoization
# #Algorithm_I_Day_12_Dynamic_Programming #Dynamic_Programming_I_Day_2
# #Level_1_Day_10_Dynamic_Programming #Udemy_Dynamic_Programming #Top_Interview_150_1D_DP
# #Big_O_Time_O(n)_Space_O(n) #2025_07_24_Time_0_ms_(100.00%)_Space_17.79_MB_(48.58%)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        # Initialize first 2 numbers of the array
        arr = [0] * n
        arr[0] = 1
        arr[1] = 2
        # Fill out the rest of the array from the first two numbers
        for i in range(2, n):
            arr[i] = arr[i - 2] + arr[i - 1]
        
        return arr[-1]
