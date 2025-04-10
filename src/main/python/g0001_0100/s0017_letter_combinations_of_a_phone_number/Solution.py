# #Medium #Top_100_Liked_Questions #Top_Interview_Questions #String #Hash_Table #Backtracking
# #Algorithm_II_Day_11_Recursion_Backtracking #Udemy_Backtracking/Recursion
# #Top_Interview_150_Backtracking #Big_O_Time_O(4^n)_Space_O(n)
# #2024_06_04_Time_28_ms_(91.85%)_Space_16.5_MB_(84.41%)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letters = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = []
        self.findCombinations(0, digits, letters, [], ans)
        return ans

    def findCombinations(self, start, digits, letters, curr, ans):
        if len(curr) == len(digits):
            ans.append("".join(curr))
            return

        for i in range(start, len(digits)):
            n = int(digits[i])
            for ch in letters[n]:
                curr.append(ch)
                self.findCombinations(i + 1, digits, letters, curr, ans)
                curr.pop()
