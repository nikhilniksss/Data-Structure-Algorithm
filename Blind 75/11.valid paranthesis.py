# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([])"
# Output: true


def valid_paranthesis(s):
    stack = []
    bracket_map = {")":"(","]":"[","}":"{"}
    
    for character in s:
        if character in bracket_map:
            if stack and stack[-1] == bracket_map[character]:
                stack.pop()
            else:
                return False
        else:
            stack.append(character)
    return not stack


s = "()"
print(valid_paranthesis(s))

s = "()[]{}"
print(valid_paranthesis(s))

s = "(]"
print(valid_paranthesis(s))

s = "([])"
print(valid_paranthesis(s))


