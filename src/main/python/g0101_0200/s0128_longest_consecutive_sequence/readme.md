128\. Longest Consecutive Sequence

Medium

Given an unsorted array of integers `nums`, return _the length of the longest consecutive elements sequence._

You must write an algorithm that runs in `O(n)` time.

**Example 1:**

**Input:** nums = [100,4,200,1,3,2]

**Output:** 4

**Explanation:** The longest consecutive elements sequence is `[1, 2, 3, 4]`. Therefore its length is 4. 

**Example 2:**

**Input:** nums = [0,3,7,2,5,8,4,6,0,1]

**Output:** 9 

**Constraints:**

*   <code>0 <= nums.length <= 10<sup>5</sup></code>
*   <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code>

To solve the "Longest Consecutive Sequence" problem in Python with a `Solution` class, we'll use a HashSet and a greedy approach. Below are the steps:

1. **Create a `Solution` class**: Define a class named `Solution` to encapsulate our solution methods.

2. **Create a `longestConsecutive` method**: This method takes an array `nums` as input and returns the length of the longest consecutive elements sequence.

3. **Initialize a HashSet**: Create a HashSet named `numSet` to store all the numbers in the array `nums`.

4. **Iterate through the array**: Add all the numbers from the array `nums` to the `numSet`.

5. **Find the longest sequence**: Iterate through the array `nums` again. For each number `num` in the array:
   - Check if `num - 1` exists in the `numSet`. If it does not, `num` could be the start of a new sequence.
   - If `num - 1` does not exist, start a new sequence from `num`. Increment `currentNum` by 1 and check if `currentNum` exists in the `numSet`. Keep incrementing `currentNum` until it does not exist in the `numSet`. Update the maximum length of the sequence accordingly.

6. **Return the maximum length**: After iterating through the entire array, return the maximum length of the consecutive sequence.

Here's the Python implementation:

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0
        
        for num in num_set:
            if num - 1 not in num_set:
                cur_num = num
                cur_length = 1
                
                while cur_num + 1 in num_set:
                    cur_num += 1
                    cur_length += 1
                
                max_length = max(max_length, cur_length)
        
        return max_length
```

This implementation follows the steps outlined above and efficiently calculates the length of the longest consecutive elements sequence in Python.