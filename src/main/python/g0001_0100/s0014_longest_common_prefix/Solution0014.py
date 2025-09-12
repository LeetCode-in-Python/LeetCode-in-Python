# #Easy #Top_Interview_Questions #String #Level_2_Day_2_String #Udemy_Strings
# #Top_Interview_150_Array/String #Big_O_Time_O(n*m)_Space_O(m)
# #2025_09_12_Time_0_ms_(100.00%)_Space_17.73_MB_(78.70%)

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 1:
            return ""
        if len(strs) == 1:
            return strs[0]
        temp = strs[0]
        i = 1
        while temp and i < len(strs):
            if len(temp) > len(strs[i]):
                temp = temp[: len(strs[i])]
            cur = strs[i][: len(temp)]
            if cur != temp:
                temp = temp[: len(temp) - 1]
            else:
                i += 1
        return temp
