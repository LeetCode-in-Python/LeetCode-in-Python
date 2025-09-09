# #Medium #String #Hash_Table #Math #Top_Interview_150_Array/String #Big_O_Time_O(1)_Space_O(1)
# #2025_09_09_Time_XX_ms_(_) _Space_XX_MB_(_)

class Solution:
    def intToRoman(self, num: int) -> str:
        sb: list[str] = []

        def numerals(remaining: int, one: int, c_ten: str, c_five: str, c_one: str) -> int:
            div = remaining // one
            if div == 9:
                sb.append(c_one)
                sb.append(c_ten)
            elif div == 8:
                sb.append(c_five)
                sb.append(c_one)
                sb.append(c_one)
                sb.append(c_one)
            elif div == 7:
                sb.append(c_five)
                sb.append(c_one)
                sb.append(c_one)
            elif div == 6:
                sb.append(c_five)
                sb.append(c_one)
            elif div == 5:
                sb.append(c_five)
            elif div == 4:
                sb.append(c_one)
                sb.append(c_five)
            elif div == 3:
                sb.append(c_one)
                sb.append(c_one)
                sb.append(c_one)
            elif div == 2:
                sb.append(c_one)
                sb.append(c_one)
            elif div == 1:
                sb.append(c_one)
            return remaining - (div * one)

        num = numerals(num, 1000, ' ', ' ', 'M')
        num = numerals(num, 100, 'M', 'D', 'C')
        num = numerals(num, 10, 'C', 'L', 'X')
        numerals(num, 1, 'X', 'V', 'I')
        return "".join(sb)
