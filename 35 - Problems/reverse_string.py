# reverse string in form of array

def reverseString(str):
    left = 0
    right = len(str)-1

    while left <= right:
        str[left], str[right] = str[right],str[left]
        left += 1
        right -= 1
    return str

str = ['n','i','k','h','i','l'] # even number
print(reverseString(str))

str = ['n','i','k','h','i','l','s'] # odd numbers
print(reverseString(str))