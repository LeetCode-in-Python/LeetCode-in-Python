# #Easy #String #Hash_Table #Data_Structure_II_Day_7_String #Top_Interview_150_Hashmap
# #2025_09_20_Time_0_ms_(100.00%)_Space_17.99_MB_(15.86%)

from typing import Dict

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map: Dict[str, str] = {}
        words = s.split()
        if len(words) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in map:
                if words[i] in map.values():
                    return False
                map[pattern[i]] = words[i]
            else:
                if words[i] != map[pattern[i]]:
                    return False
        return True
