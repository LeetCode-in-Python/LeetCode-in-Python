17\. Letter Combinations of a Phone Number

Medium

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in **any order**.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png)

**Example 1:**

**Input:** digits = "23"

**Output:** ["ad","ae","af","bd","be","bf","cd","ce","cf"] 

**Example 2:**

**Input:** digits = ""

**Output:** [] 

**Example 3:**

**Input:** digits = "2"

**Output:** ["a","b","c"] 

**Constraints:**

*   `0 <= digits.length <= 4`
*   `digits[i]` is a digit in the range `['2', '9']`.

Here are the steps to solve the "Letter Combinations of a Phone Number" problem:

### Approach:

1. **Define Letter Mapping:**
   - Define a dictionary mapping each digit to its corresponding letters on the telephone keypad.

2. **Initialize Result List:**
   - Initialize an empty list `result` to store the letter combinations.

3. **Check for Empty Input:**
   - If the input string `digits` is empty, return an empty list.

4. **Recursive Backtracking:**
   - Use a recursive backtracking approach to generate all possible combinations.
     - Define a recursive function that takes the current combination, current index, and the result list as parameters.
     - Base case: If the current combination length is equal to the length of the input `digits`, add it to the result list.
     - For the current digit, get its corresponding letters and recursively call the function for each letter with an updated combination and index.

5. **Return Result List:**
   - Return the final list of letter combinations.

### Python Code:

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Define letter mapping
        letter_mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        # Initialize result list
        result = []

        # Base case: empty input
        if not digits:
            return result

        # Recursive backtracking function
        def backtrack(combination, index):
            # Base case: combination length equals digits length
            if index == len(digits):
                result.append(''.join(combination))
                return

            # Get letters for current digit
            current_digit = digits[index]
            for letter in letter_mapping[current_digit]:
                # Recursively call with updated combination and index
                combination.append(letter)
                backtrack(combination, index + 1)
                combination.pop()

        # Start recursive backtracking
        backtrack([], 0)

        return result

# Example Usage:
solution = Solution()

# Example 1:
digits1 = "23"
print(solution.letterCombinations(digits1))  # Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example 2:
digits2 = ""
print(solution.letterCombinations(digits2))  # Output: []

# Example 3:
digits3 = "2"
print(solution.letterCombinations(digits3))  # Output: ["a","b","c"]
```

This code defines a `Solution` class with a method `letterCombinations` that takes a string of digits as input and returns a list of all possible letter combinations. The example usage demonstrates how to create an instance of the `Solution` class and call the `letterCombinations` method with different inputs.