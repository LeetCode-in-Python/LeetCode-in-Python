# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #Array #String #Hash_Table #Sorting
# #Data_Structure_II_Day_8_String #Programming_Skills_II_Day_11 #Udemy_Strings
# #Top_Interview_150_Hashmap #Big_O_Time_O(n*k_log_k)_Space_O(n)
# #2025_07_24_Time_11_ms_(82.75%)_Space_20.85_MB_(56.49%)

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)
        for s in strs:
            sorted_str = ''.join(sorted(s))
            anagram_groups[sorted_str].append(s)
        return list(anagram_groups.values())
