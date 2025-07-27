# Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".
# A string is palindromic if it reads the same forward and backward.

 
# Example 1:
# Input: words = ["abc","car","ada","racecar","cool"]
# Output: "ada"
# Explanation: The first string that is palindromic is "ada".
# Note that "racecar" is also palindromic, but it is not the first.

# Example 2:
# Input: words = ["notapalindrome","racecar"]
# Output: "racecar"
# Explanation: The first and only string that is palindromic is "racecar".

# Example 3:
# Input: words = ["def","ghi"]
# Output: ""
# Explanation: There are no palindromic strings, so the empty string is returned.



def first_palindrome(words):
    for word in words:
        left = 0
        right = len(word) - 1
        is_palindrome = True
        while left < right:
            if word[left] != word[right]:
                is_palindrome = False
            left += 1
            right -= 1
        if is_palindrome:
            return word
    return ""
        
words = ["notapalindrome","racecar"]
print(first_palindrome(words))

words = ["abc","car","ada","racecar","cool"]
print(first_palindrome(words))



        
        