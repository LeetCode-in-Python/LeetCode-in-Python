# #Easy #Top_Interview_Questions #Hash_Table #Math #Two_Pointers #Algorithm_II_Day_21_Others
# #Programming_Skills_I_Day_4_Loop #Level_2_Day_1_Implementation/Simulation
# #Top_Interview_150_Hashmap #2025_09_14_Time_0_ms_(100.00%)_Space_17.98_MB_(18.11%)

class Solution:
    def isHappy(self, n: int) -> bool:
        happy = False
        a = n
        sum_val = 0
        if a == 1 or a == 7:
            happy = True
        elif 1 < a < 10:
            happy = False
        else:
            while a != 0:
                rem = a % 10
                sum_val = sum_val + (rem * rem)
                a = a # 10
            if sum_val != 1:
                happy = self.isHappy(sum_val)
            else:
                happy = True
        return happy

