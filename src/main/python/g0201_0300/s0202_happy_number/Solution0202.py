# #Easy #Top_Interview_Questions #Hash_Table #Math #Two_Pointers #Algorithm_II_Day_21_Others
# #Programming_Skills_I_Day_4_Loop #Level_2_Day_1_Implementation/Simulation
# #Top_Interview_150_Hashmap #2025_09_15_Time_0_ms_(100.00%)_Space_17.57_MB_(97.85%)

class Solution:
    def isHappy(self, n: int) -> bool:
        a = n
        rem = 0
        sum_val = 0        
        if a == 1 or a == 7:
            return True
        elif 1 < a < 10:
            return False
        else:
            while a != 0:
                rem = a % 10
                sum_val += rem * rem
                a //= 10
            if sum_val != 1:
                return self.isHappy(sum_val)
            else:
                return True
