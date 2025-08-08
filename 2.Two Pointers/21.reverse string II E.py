# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.
# If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.


# Example 1:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"


# Example 2:
# Input: s = "abcd", k = 2
# Output: "bacd"

def reverse_string(s,k):
    n = len(s)
    s = list(s)
    for i in range(0,n,2*k):
        s[i:i+k] = reversed(s[i:i+k])
    return "".join(s)

s = "abcdefg"
k = 2
print(reverse_string(s,k))

s = "abcd"
k = 2
print(reverse_string(s,k))