# #Medium #Top_100_Liked_Questions #String #Hash_Table #Greedy #Two_Pointers
# #Data_Structure_II_Day_7_String #Big_O_Time_O(n)_Space_O(1)
# #2025_07_25_Time_5_ms_(53.34%)_Space_17.62_MB_(84.14%)

from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letters = list(s)
        result = []
        position = [0] * 26

        for i in range(len(letters)):
            position[ord(letters[i]) - ord('a')] = i

        i = 0
        prev = -1
        max_pos = 0

        while i < len(letters):
            if position[ord(letters[i]) - ord('a')] > max_pos:
                max_pos = position[ord(letters[i]) - ord('a')]
            if i == max_pos:
                result.append(i - prev)
                prev = i
            i += 1

        return result
