# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
# Note that after backspacing an empty text, the text will continue empty.


# Example 1:
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".


# Example 2:
# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".


# Example 3:
# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".

# stack based

def backspace(s,t):
    def build(string):
        stack = []
        for char in string:
            if char != "#":
                stack.append(char)
            elif stack:
                stack.pop()
        return ''.join(stack)
    return build(s) == build(t)


s = "ab#c"
t = "ad#c"
print(backspace(s,t))

