136\. Single Number

Easy

Given a **non-empty** array of integers `nums`, every element appears _twice_ except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

**Example 1:**

**Input:** nums = [2,2,1]

**Output:** 1 

**Example 2:**

**Input:** nums = [4,1,2,1,2]

**Output:** 4 

**Example 3:**

**Input:** nums = [1]

**Output:** 1 

**Constraints:**

*   <code>1 <= nums.length <= 3 * 10<sup>4</sup></code>
*   <code>-3 * 10<sup>4</sup> <= nums[i] <= 3 * 10<sup>4</sup></code>
*   Each element in the array appears twice except for one element which appears only once.

To solve this problem with the `Solution` class, which requires linear runtime complexity and constant extra space, we can utilize the bitwise XOR operation. Here are the steps:

1. Define the `Solution` class with a method `singleNumber` that takes a list of integers `nums` as input and returns the single number that appears only once.
2. Within the `singleNumber` method, initialize a variable `result` to 0.
3. Iterate through each element in the `nums` list.
4. Perform bitwise XOR operation between `result` and the current element.
5. After iterating through all elements, `result` will contain the single number that appears only once due to the properties of XOR operation.
6. Finally, return the `result`.

Here's how the `Solution` class would look like in Python:

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result

# Example usage:
solution = Solution()
print(solution.singleNumber([2, 2, 1]))      # Output: 1
print(solution.singleNumber([4, 1, 2, 1, 2]))# Output: 4
print(solution.singleNumber([1]))            # Output: 1
```

This solution leverages the bitwise XOR operation to find the single number that appears only once in the array, achieving linear runtime complexity and constant extra space usage.