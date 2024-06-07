# #Medium #String #Hash_Table #Greedy #Two_Pointers #Data_Structure_II_Day_7_String
# #Big_O_Time_O(n)_Space_O(1) #2024_06_07_Time_32_ms_(95.28%)_Space_16.4_MB_(98.19%)

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
