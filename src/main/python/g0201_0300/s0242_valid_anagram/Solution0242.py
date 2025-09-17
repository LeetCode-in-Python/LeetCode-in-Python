# #Easy #String #Hash_Table #Sorting #Data_Structure_I_Day_6_String
# #Programming_Skills_I_Day_11_Containers_and_Libraries #Udemy_Strings #Top_Interview_150_Hashmap
# #2025_09_17_Time_11_ms_(72.46%)_Space_17.66_MB_(97.60%)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1
        for ch in t:
            idx = ord(ch) - 97
            if freq[idx] == 0:
                return False
            freq[idx] -= 1
        return True
