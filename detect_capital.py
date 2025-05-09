# check if the word uses proper uses of capital

# valid capital:
# 1. All are capital e.g. TEST
# 2. All letters are small e.g. test
# 3. First letter is capital and rest are small e.g. Test

def detectCapital(word):
    count = 0
    length = len(word)

    for i in range(length):
        if word[i] >= chr(65) and word[i] < chr(91):
            count += 1

    if count == length:
        return True
    elif count == 0:
        return True
    elif count == 1 and word[0] >= chr(65) and word[0] < chr(91):
        return True
    else:
        return False

print(detectCapital("USA"))
print(detectCapital("Usa"))
print(detectCapital("usa"))
print(detectCapital("uSa"))
print(detectCapital("UsA"))
print(detectCapital("uSA"))
