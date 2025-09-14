# #Hard #Array #Greedy #Top_Interview_150_Array/String
# #2025_09_14_Time_7_ms_(97.91%)_Space_19.79_MB_(91.21%)

from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)
        for i in range(len(ratings) - 1):
            if ratings[i + 1] > ratings[i]:
                candies[i + 1] = candies[i] + 1
        for i in range(len(ratings) - 1, 0, -1):
            if ratings[i - 1] > ratings[i] and candies[i - 1] < candies[i] + 1:
                candies[i - 1] = candies[i] + 1
        return sum(candies)
