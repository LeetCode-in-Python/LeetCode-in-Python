# #Easy #Top_100_Liked_Questions #Top_Interview_Questions #Array #Hash_Table #Sorting #Counting
# #Divide_and_Conquer #Data_Structure_II_Day_1_Array #Udemy_Famous_Algorithm
# #Big_O_Time_O(n)_Space_O(1) #2024_06_09_Time_170_ms_(59.75%)_Space_18_MB_(27.19%)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        majority = arr[0]

        # For Potential Majority Element
        for i in range(1, len(arr)):
            if arr[i] == majority:
                count += 1
            else:
                if count > 1:
                    count -= 1
                else:
                    majority = arr[i]

        # For Confirmation
        count = 0
        for j in arr:
            if j == majority:
                count += 1

        if count >= (len(arr) // 2) + 1:
            return majority
        else:
            return -1
