# #Hard #Array #String #Simulation #Top_Interview_150_Array/String
# #2025_09_13_Time_0_ms_(100.00%)_Space_17.85_MB_(62.97%)

from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # Trying to gauge the number of lines so the list doesn't need to resize
        output = []
        # Setting string capacity also
        sb = []
        line_total = 0
        num_words_on_line = 0
        start_word = 0
        # looping until the 2nd last word, since we're checking words[i + 1] for overflows
        for i in range(len(words) - 1):
            line_total += len(words[i])
            # tracking line length + #words
            num_words_on_line += 1
            # checking if the next word causes an overflow
            if line_total + num_words_on_line + len(words[i + 1]) > maxWidth:
                # if only one word fits on the line...
                if num_words_on_line == 1:
                    # append word
                    sb.append(words[i])
                    # pad right with spaces
                    while line_total < maxWidth:
                        sb.append(' ')
                        line_total += 1
                else:
                    # # of extra spaces
                    extra_sp = (maxWidth - line_total) % (num_words_on_line - 1)
                    # Creating the line
                    for j in range(start_word, start_word + num_words_on_line - 1):
                        # appending the word
                        sb.append(words[j])
                        if extra_sp > 0:
                            # appending an extra space, if required
                            sb.append(' ')
                            extra_sp -= 1
                        # appending the rest of the required spaces
                        max_spaces = max(0, (maxWidth - line_total) // (num_words_on_line - 1))
                        sb.append(' ' * max_spaces)
                    # appending the last word of the line
                    sb.append(words[start_word + num_words_on_line - 1])
                # adding to output list
                output.append(''.join(sb))
                # reset everything for next line
                # keeping track of the first word for next line
                start_word = i + 1
                # resetting these to 0 for processing next line
                num_words_on_line = line_total = 0
                # need a new list for the next line
                sb = []
        # handling the final line (no justification, right padded with spaces)
        line_total = 0
        for i in range(start_word, len(words)):
            line_total += len(words[i])
            sb.append(words[i])
            if line_total < maxWidth:
                sb.append(' ')
                line_total += 1
        # padding right side with spaces
        while line_total < maxWidth:
            sb.append(' ')
            line_total += 1
        # add the final line to output list
        output.append(''.join(sb))
        return output
