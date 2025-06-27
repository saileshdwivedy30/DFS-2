# Time Complexity : O(n), where n is the length of the input string
# Space Complexity : O(n), for stacks used in decoding
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach

# I used two stacks: one for counts and one for strings to handle nested structures

class Solution:
    def decodeString(self, s: str) -> str:
        count_stack = []
        string_stack = []
        current_string = ""
        current_num = 0

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                count_stack.append(current_num)
                string_stack.append(current_string)
                current_num = 0
                current_string = ""
            elif char == ']':
                repeat = count_stack.pop()
                prev_string = string_stack.pop()
                current_string = prev_string + current_string * repeat
            else:
                current_string += char

        return current_string
