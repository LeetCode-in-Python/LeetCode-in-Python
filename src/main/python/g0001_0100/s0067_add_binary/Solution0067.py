# #Easy #String #Math #Bit_Manipulation #Simulation #Programming_Skills_II_Day_5
# #Top_Interview_150_Bit_Manipulation #2025_09_13_Time_0_ms_(100.00%)_Space_17.78_MB_(73.57%)

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        deci_a = int(a, 2) # Here I used the int function built-in in python and set the base to be 2 so it knows which base it is
        deci_b = int(b, 2)
        both_summed = deci_a + deci_b
        if both_summed == 0:
            return "0"
        binary_form = []
        while both_summed > 0:
            remainder = both_summed % 2
            binary_form.insert(0, str(remainder)) # Here I used insert so I could insert at first index so i wouldnt have to reverse it
            both_summed //= 2

        return "".join(binary_form) # Here I had to use join i could use print beacause leetcodes expects returned value so I use "" as seperator and joined the variable
