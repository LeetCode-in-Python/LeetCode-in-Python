198\. House Robber

Medium

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given an integer array `nums` representing the amount of money of each house, return _the maximum amount of money you can rob tonight **without alerting the police**_.

**Example 1:**

**Input:** nums = [1,2,3,1]

**Output:** 4

**Explanation:**

    Rob house 1 (money = 1) and then rob house 3 (money = 3).
    Total amount you can rob = 1 + 3 = 4. 

**Example 2:**

**Input:** nums = [2,7,9,3,1]

**Output:** 12

**Explanation:**

    Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
    Total amount you can rob = 2 + 9 + 1 = 12. 

**Constraints:**

*   `1 <= nums.length <= 100`
*   `0 <= nums[i] <= 400`

To solve the House Robber problem, we can utilize dynamic programming to find the maximum amount of money we can rob without alerting the police. Here's how we can approach this problem:

1. **Initialize Variables**:
   - Initialize two variables, `prev_max` and `curr_max`, to keep track of the maximum amount of money robbed from previous houses and the current house, respectively.

2. **Iterate Through Houses**:
   - Iterate through the array of house values `nums`.
   
3. **Calculate Maximum Amount of Money Robbed**:
   - For each house, update `curr_max` to the maximum value between the sum of the value of the current house and `prev_max`, and `prev_max`.
   
4. **Return Result**:
   - After iterating through all houses, return `curr_max`, which represents the maximum amount of money that can be robbed without alerting the police.

Let's implement this approach:

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        prev_max = curr_max = 0
        
        for num in nums:
            temp = curr_max
            curr_max = max(prev_max + num, curr_max)
            prev_max = temp
        
        return curr_max
```

This solution ensures that we calculate the maximum amount of money that can be robbed without alerting the police in linear time complexity O(n) and constant space complexity O(1), meeting the problem constraints.