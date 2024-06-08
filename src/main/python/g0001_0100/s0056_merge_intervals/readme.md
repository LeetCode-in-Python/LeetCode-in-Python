56\. Merge Intervals

Medium

Given an array of `intervals` where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>, merge all overlapping intervals, and return _an array of the non-overlapping intervals that cover all the intervals in the input_.

**Example 1:**

**Input:** intervals = [[1,3],[2,6],[8,10],[15,18]]

**Output:** [[1,6],[8,10],[15,18]]

**Explanation:** Since intervals [1,3] and [2,6] overlaps, merge them into [1,6]. 

**Example 2:**

**Input:** intervals = [[1,4],[4,5]]

**Output:** [[1,5]]

**Explanation:** Intervals [1,4] and [4,5] are considered overlapping. 

**Constraints:**

*   <code>1 <= intervals.length <= 10<sup>4</sup></code>
*   `intervals[i].length == 2`
*   <code>0 <= start<sub>i</sub> <= end<sub>i</sub> <= 10<sup>4</sup></code>

Here are the steps to solve the task using the `Solution` class:

1. Define the `Solution` class with a method named `merge` that takes in a list of intervals.
2. Inside the `merge` method, sort the intervals based on their start times.
3. Initialize an empty list called `merged_intervals` to store the merged intervals.
4. Iterate through the sorted intervals.
5. For each interval, if the `merged_intervals` list is empty or if the current interval's start time is greater than the end time of the last interval in the `merged_intervals` list, append the current interval to `merged_intervals`.
6. Otherwise, merge the current interval with the last interval in the `merged_intervals` list by updating the end time of the last interval if the current interval's end time is greater.
7. After iterating through all intervals, return the `merged_intervals` list.

Here's the implementation:

```python
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged_intervals = []
        
        for interval in intervals:
            if not merged_intervals or interval[0] > merged_intervals[-1][1]:
                merged_intervals.append(interval)
            else:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
        
        return merged_intervals

# Example usage:
intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals2 = [[1, 4], [4, 5]]

sol = Solution()
print(sol.merge(intervals1))  # Output: [[1, 6], [8, 10], [15, 18]]
print(sol.merge(intervals2))  # Output: [[1, 5]]
```