9\. Palindrome Number

Easy

Given an integer `x`, return `true` if `x` is palindrome integer.

An integer is a **palindrome** when it reads the same backward as forward. For example, `121` is palindrome while `123` is not.

**Example 1:**

**Input:** x = 121

**Output:** true 

**Example 2:**

**Input:** x = -121

**Output:** false

**Explanation:** From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome. 

**Example 3:**

**Input:** x = 10

**Output:** false

**Explanation:** Reads 01 from right to left. Therefore it is not a palindrome. 

**Example 4:**

**Input:** x = -101

**Output:** false 

**Constraints:**

*   <code>-2<sup>31</sup> <= x <= 2<sup>31</sup> - 1</code>

**Follow up:** Could you solve it without converting the integer to a string?

Here are the steps to solve the "Palindrome Number" problem:

### Approach:

1. **Handle Special Cases for Negative Numbers:**
   - If the given integer `x` is negative, return `false` since negative numbers cannot be palindromes.

2. **Reverse the Integer:**
   - Reverse the digits of the positive integer `x` to obtain a new integer.

3. **Check for Palindrome:**
   - Compare the reversed integer with the original integer `x`.
   - If they are equal, return `true`; otherwise, return `false`.

4. **Return Result:**
   - Return the result indicating whether the integer is a palindrome or not.

### Python Code:

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Handle special case for negative numbers
        if x < 0:
            return False

        # Reverse the digits of the positive integer
        reversed_x = self.reverse(x)

        # Check for palindrome
        return x == reversed_x

    def reverse(self, x: int) -> int:
        reversed_x = 0
        while x > 0:
            digit = x % 10
            reversed_x = reversed_x * 10 + digit
            x //= 10
        return reversed_x

# Example Usage:
solution = Solution()

# Example 1:
x1 = 121
print(solution.isPalindrome(x1))  # Output: True

# Example 2:
x2 = -121
print(solution.isPalindrome(x2))  # Output: False

# Example 3:
x3 = 10
print(solution.isPalindrome(x3))  # Output: False

# Example 4:
x4 = -101
print(solution.isPalindrome(x4))  # Output: False
```

This code defines a `Solution` class with a method `isPalindrome` that takes an integer `x` as input and returns `True` if it is a palindrome and `False` otherwise. The example usage demonstrates how to create an instance of the `Solution` class and call the `isPalindrome` method with different inputs. The `reverse` method is used to reverse the digits of a positive integer.