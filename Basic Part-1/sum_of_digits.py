'''68. Write a Python program to calculate sum of digits of a number.
'''

def sumdigits(num):

    sum = 0
    for _ in num:
        _ = int(_)
        sum += _
    return sum


num = input("Enter a number: ")
print(sumdigits(num))