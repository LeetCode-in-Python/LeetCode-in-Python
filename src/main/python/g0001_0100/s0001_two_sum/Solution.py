# #Easy #Top_100_Liked_Questions #Top_Interview_Questions #Array #Hash_Table
# #Data_Structure_I_Day_2_Array #Level_1_Day_13_Hashmap #Udemy_Arrays #Top_Interview_150_Hashmap
# #Big_O_Time_O(n)_Space_O(n) #AI_can_be_used_to_solve_the_task
# #2024_06_06_Time_62_ms_(53.52%)_Space_17.8_MB_(37.79%)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index_map = {}
        for i, num in enumerate(numbers):
            required_num = target - num
            if required_num in index_map:
                return [index_map[required_num], i]
            index_map[num] = i
        return [-1, -1]
