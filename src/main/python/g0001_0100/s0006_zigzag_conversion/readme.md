6\. Zigzag Conversion

Medium

The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P A H N A P L S I I G Y I R 

And then read line by line: `"PAHNAPLSIIGYIR"`

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows); 

**Example 1:**

**Input:** s = "PAYPALISHIRING", numRows = 3

**Output:** "PAHNAPLSIIGYIR" 

**Example 2:**

**Input:** s = "PAYPALISHIRING", numRows = 4

**Output:** "PINALSIGYAHRPI"

**Explanation:** P I N A L S I G Y A H R P I 

**Example 3:**

**Input:** s = "A", numRows = 1

**Output:** "A" 

**Constraints:**

*   `1 <= s.length <= 1000`
*   `s` consists of English letters (lower-case and upper-case), `','` and `'.'`.
*   `1 <= numRows <= 1000`

Here are the steps to solve the "Zigzag Conversion" problem:

### Approach:

1. **Handle Special Cases:**
   - If the number of rows (`numRows`) is 1 or the length of the string (`s`) is less than or equal to the number of rows, return the original string.

2. **Initialize Rows:**
   - Create a list of strings to represent each row of the zigzag pattern.
   - Initialize an index variable to keep track of the current row.

3. **Iterate through the String:**
   - Iterate through each character in the string `s`.

4. **Fill Rows:**
   - For each character, determine the current row in the zigzag pattern.
   - Append the character to the corresponding row.

5. **Read Zigzag Pattern:**
   - Concatenate the rows to obtain the final zigzag pattern.

6. **Return Result:**
   - Return the final zigzag pattern.

### Python Code:

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Handle special cases
        if numRows == 1 or len(s) <= numRows:
            return s

        # Initialize rows
        rows = [''] * numRows
        index = 0
        direction = 1  # 1 for down, -1 for up

        # Iterate through the string
        for char in s:
            # Fill rows
            rows[index] += char

            # Change direction if reaching top or bottom row
            if index == 0:
                direction = 1
            elif index == numRows - 1:
                direction = -1

            # Move to the next row
            index += direction

        # Read zigzag pattern
        result = ''.join(rows)

        # Return the final result
        return result

# Example Usage:
solution = Solution()

# Example 1:
s1 = "PAYPALISHIRING"
numRows1 = 3
print(solution.convert(s1, numRows1))  # Output: "PAHNAPLSIIGYIR"

# Example 2:
s2 = "PAYPALISHIRING"
numRows2 = 4
print(solution.convert(s2, numRows2))  # Output: "PINALSIGYAHRPI"

# Example 3:
s3 = "A"
numRows3 = 1
print(solution.convert(s3, numRows3))  # Output: "A"
```

This code defines a `Solution` class with a method `convert` that takes a string `s` and the number of rows `numRows` as input and returns the zigzag conversion of the string. The example usage demonstrates how to create an instance of the `Solution` class and call the `convert` method with different inputs.