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

# Example 5:
# Input: s = "([)]"
# Output: false

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

# brute force method

# def valid_paranthesis(s):
#     while "()" in s or "{}" in s or "[]" in s:
#         s = s.replace("()","")
#         s = s.replace("[]]","")
#         s = s.replace("{}","")
#     return s == ""


# # s = "()"
# # print(valid_paranthesis(s))

# s = "()[]{}"
# print(valid_paranthesis(s))

# # s = "(]"
# # print(valid_paranthesis(s))

# # s = "([])"
# # print(valid_paranthesis(s))

# # s = "([)]"
# # print(valid_paranthesis(s))

def valid_paranthesis(s):
    stack = []
    mapping = {"}":"{","]":"[",")":"("}

    for ch in s:
        if ch in mapping:
            if stack and stack[-1] == mapping[ch]:
                stack.pop()
            else:
                return False
        else:
            stack.append(ch)
    return True if not stack else False

s = "()"
print(valid_paranthesis(s))

s = "()[]{}"
print(valid_paranthesis(s))

s = "(]"
print(valid_paranthesis(s))

s = "([])"
print(valid_paranthesis(s))

s = "([)]"
print(valid_paranthesis(s))