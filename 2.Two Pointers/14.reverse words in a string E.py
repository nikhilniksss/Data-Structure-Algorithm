# Given a string s, reverse the order of characters in each word within a sentence 
# while still preserving whitespace and initial word order.

# Example 1:
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

# Example 2:
# Input: s = "Mr Ding"
# Output: "rM gniD"


def reverse_string(s):
    result = []
    for word in s.split():
        word = list(word)
        left, right = 0, len(word) - 1
        while left < right:
            word[left], word[right] = word[right],word[left]
            left += 1
            right -= 1
        result.append("".join(word))
    return " ".join(result)

s = "Mr Ding"
print(reverse_string(s))

s = "Let's take LeetCode contest"
print(reverse_string(s))
