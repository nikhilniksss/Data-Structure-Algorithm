# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original 
# list of strings.

# Please implement encode and decode

# Example 1:
# Input: ["neet","code","love","you"]
# Output:["neet","code","love","you"]

# Example 2:
# Input: ["we","say",":","yes"]
# Output: ["we","say",":","yes"]

class solution:
    def encode(self,strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    
    def decode(self,s):
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j + 1 + length
        return res

if __name__ == "__main__":
    sol = solution()

    words = ["neet","code","love","you"]
    encoded = sol.encode(words)
    decoded = sol.decode(encoded)

    print("Original:",words)
    print("Encoded:",encoded)
    print("Decoded:",decoded)



