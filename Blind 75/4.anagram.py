# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:

# Input: s = "rat", t = "car"
# Output: false


def anagram_program(str1,str2):

    str1 = str1.lower()
    str2 = str2.lower()

    str1 = str1.replace(" ","")
    str2 = str2.replace(" ","")

    count = [0] * 26

    for char in str1:
        count[ord(char) - ord('a')] += 1

    for char in str2:
        count[ord(char) - ord('a')] -= 1

    for ele in count:
        if ele != 0:
            return False
    return True


s = "anagram", t = "nagaram"
print(anagram_program(s,t))

s = "rat", t = "car"
print(anagram_program(s,t))
