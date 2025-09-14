# #Easy #String #Hash_Table #Level_1_Day_2_String #Top_Interview_150_Hashmap
# #2025_09_14_Time_3_ms_(95.32%)_Space_18.38_MB_(7.18%)

from typing import List

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_array = [0] * 128
        str_chars = list(s)
        tar_chars = list(t)
        n = len(str_chars)
        for i in range(n):
            if map_array[ord(tar_chars[i])] == 0:
                if self._search(map_array, ord(str_chars[i]), ord(tar_chars[i])) != -1:
                    return False
                map_array[ord(tar_chars[i])] = ord(str_chars[i])
            else:
                if map_array[ord(tar_chars[i])] != ord(str_chars[i]):
                    return False
        return True

    def _search(self, map_array: List[int], target: int, skip: int) -> int:
        for i in range(128):
            if i == skip:
                continue
            if map_array[i] != 0 and map_array[i] == target:
                return i
        return -1
