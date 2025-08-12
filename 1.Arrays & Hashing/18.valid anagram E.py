# Given two strings s and t, return true if t is an anagram of s, and false otherwise.


# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

def check_anagram(s,t):
    if len(s) != len(t):
        return False
    
    count = [0] * 26
    for i in range(len(s)):
        count[ord(s[i]) - ord("a")] += 1
        count[ord(t[i]) - ord("a")] -= 1

    for val in count:
        if val != 0:
            return False
    return True


s = "anagram"
t = "nagaram"
print(check_anagram(s,t))

s = "rat"
t = "car"
print(check_anagram(s,t))


