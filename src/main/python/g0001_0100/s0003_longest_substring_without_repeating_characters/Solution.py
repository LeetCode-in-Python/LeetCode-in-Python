# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #String #Hash_Table #Sliding_Window
# #Algorithm_I_Day_6_Sliding_Window #Level_2_Day_14_Sliding_Window/Two_Pointer #Udemy_Strings
# #Top_Interview_150_Sliding_Window #Big_O_Time_O(n)_Space_O(1) #AI_can_be_used_to_solve_the_task
# #2024_06_06_Time_45_ms_(93.32%)_Space_16.6_MB_(53.05%)

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
