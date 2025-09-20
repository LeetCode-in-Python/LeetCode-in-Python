# #Easy #String #Dynamic_Programming #Two_Pointers #LeetCode_75_Two_Pointers
# #Dynamic_Programming_I_Day_19 #Level_1_Day_2_String #Udemy_Two_Pointers
# #Top_Interview_150_Two_Pointers #2025_09_20_Time_0_ms_(100.00%)_Space_17.66_MB_(91.76%)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        n = len(t)
        m = len(s)
        if m == 0:
            return True
        while j < n:
            if s[i] == t[j]:
                i += 1
                if i == m:
                    return True
            j += 1
        return False
