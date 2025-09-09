# #Easy #Top_Interview_Questions #String #Hash_Table #Math #Top_Interview_150_Array/String
# #Big_O_Time_O(n)_Space_O(1)

class Solution:
    def romanToInt(self, s: str) -> int:
        x = 0
        for i, ch in enumerate(s):
            if ch == 'I':
                x = self._accumulate(s, x, i, 1, 'V', 'X')
            elif ch == 'V':
                x += 5
            elif ch == 'X':
                x = self._accumulate(s, x, i, 10, 'L', 'C')
            elif ch == 'L':
                x += 50
            elif ch == 'C':
                x = self._accumulate(s, x, i, 100, 'D', 'M')
            elif ch == 'D':
                x += 500
            elif ch == 'M':
                x += 1000
        return x

    def _accumulate(self, s: str, x: int, i: int, unit: int, five: str, ten: str) -> int:
        if i + 1 == len(s):
            x += unit
        elif s[i + 1] == five:
            x -= unit
        elif s[i + 1] == ten:
            x -= unit
        else:
            x += unit
        return x
