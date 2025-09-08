# Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

# Example 1:
# Input: n = 11
# Output: 3
# Explanation:
# The input binary string 1011 has a total of three set bits.

# Example 2:
# Input: n = 128
# Output: 1
# Explanation:
# The input binary string 10000000 has a total of one set bit.

# Example 3:
# Input: n = 2147483645
# Output: 30
# Explanation:
# The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

def hammingWeight(n):
    res = 0
    while n:
        n = n & (n - 1)
        res += 1
    return res

n = 11
print(hammingWeight(n))

n = 128
print(hammingWeight(n))

n = 2147483645
print(hammingWeight(n))