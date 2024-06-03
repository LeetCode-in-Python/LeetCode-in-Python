# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #String #Hash_Table #Sliding_Window
# #Algorithm_I_Day_6_Sliding_Window #Level_2_Day_14_Sliding_Window/Two_Pointer #Udemy_Strings
# #Big_O_Time_O(n)_Space_O(1) #2024_06_03_Time_43_ms_(96.08%)_Space_16.5_MB_(92.45%)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_indices = [-1] * 256
        max_len = 0
        cur_len = 0
        start = 0

        for i, char in enumerate(s):
            if last_indices[ord(char)] < start:
                last_indices[ord(char)] = i
                cur_len += 1
            else:
                last_index = last_indices[ord(char)]
                start = last_index + 1
                cur_len = i - start + 1
                last_indices[ord(char)] = i

            if cur_len > max_len:
                max_len = cur_len

        return max_len
