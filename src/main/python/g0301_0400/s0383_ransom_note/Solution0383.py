# #Easy #String #Hash_Table #Counting #Data_Structure_I_Day_6_String #Top_Interview_150_Hashmap
# #2025_09_20_Time_11_ms_(89.85%)_Space_17.93_MB_(54.38%)

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = [0] * 26
        n = len(ransomNote)
        for i in range(n):
            freq[ord(ransomNote[i]) - 97] += 1
        for i in range(len(magazine)):
            if n == 0:
                break
            if freq[ord(magazine[i]) - 97] > 0:
                n -= 1
                freq[ord(magazine[i]) - 97] -= 1
        return n == 0
