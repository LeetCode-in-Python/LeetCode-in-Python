# #Easy #Math #Udemy_Integers #Top_Interview_150_Math #Big_O_Time_O(log10(x))_Space_O(1)
# #2025_07_22_Time_4_ms_(80.28%)_Space_17.98_MB_(19.56%)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
