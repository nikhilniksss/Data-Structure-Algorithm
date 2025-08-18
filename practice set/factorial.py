# factorial of the number

def factorial(num):
    if num == 0:  # base case
        return 1
    else:
        return num * factorial(num-1) # recursive call


num = 5
print(factorial(num))

#output - 120