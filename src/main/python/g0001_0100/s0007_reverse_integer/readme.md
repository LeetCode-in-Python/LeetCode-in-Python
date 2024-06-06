7\. Reverse Integer

Medium

Given a signed 32-bit integer `x`, return `x` _with its digits reversed_. If reversing `x` causes the value to go outside the signed 32-bit integer range <code>[-2<sup>31</sup>, 2<sup>31</sup> - 1]</code>, then return `0`.

**Assume the environment does not allow you to store 64-bit integers (signed or unsigned).**

**Example 1:**

**Input:** x = 123

**Output:** 321 

**Example 2:**

**Input:** x = -123

**Output:** -321 

**Example 3:**

**Input:** x = 120

**Output:** 21 

**Example 4:**

**Input:** x = 0

**Output:** 0 

**Constraints:**

*   <code>-2<sup>31</sup> <= x <= 2<sup>31</sup> - 1</code>

Here are the steps to solve the "Reverse Integer" problem:

### Approach:

1. **Handle Special Case for 0:**
   - If the given integer `x` is 0, return 0.

2. **Determine Sign:**
   - Determine the sign of the integer `x` (positive or negative).

3. **Handle Negative Case:**
   - If `x` is negative, update the sign and make `x` positive for the reversal process.

4. **Reverse the Digits:**
   - Convert the positive `x` to a string.
   - Reverse the string.

5. **Handle Leading Zeros:**
   - Remove leading zeros from the reversed string.

6. **Convert Back to Integer:**
   - Convert the reversed string back to an integer.

7. **Apply Sign:**
   - If the original `x` was negative, apply the negative sign to the reversed integer.

8. **Check for Overflow:**
   - Check if the reversed integer is within the 32-bit integer range <code>[-2<sup>31</sup>, 2<sup>31</sup> - 1]</code>.
   - If not, return 0.

9. **Return Result:**
   - Return the reversed integer.

### Python Code:

```python
class Solution:
    def reverse(self, x: int) -> int:
        # Handle special case for 0
        if x == 0:
            return 0

        # Determine sign
        sign = 1 if x > 0 else -1

        # Make x positive for the reversal process
        x = abs(x)

        # Reverse the digits
        reversed_str = str(x)[::-1]

        # Remove leading zeros
        reversed_str = reversed_str.lstrip('0')

        # Convert back to integer
        reversed_int = int(reversed_str)

        # Apply sign
        reversed_int *= sign

        # Check for overflow
        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            return 0

        # Return the reversed integer
        return reversed_int

# Example Usage:
solution = Solution()

# Example 1:
x1 = 123
print(solution.reverse(x1))  # Output: 321

# Example 2:
x2 = -123
print(solution.reverse(x2))  # Output: -321

# Example 3:
x3 = 120
print(solution.reverse(x3))  # Output: 21

# Example 4:
x4 = 0
print(solution.reverse(x4))  # Output: 0
```

This code defines a `Solution` class with a method `reverse` that takes an integer `x` as input and returns the reversed integer. The example usage demonstrates how to create an instance of the `Solution` class and call the `reverse` method with different inputs.