'''16. Write a Python program to calculate the difference between a given number and 17. 
If the number is greater than 17, return twice the absolute difference.
'''


def diff_17(n):

    if n > 17:
        return abs(n-17)* 2
    else:
        return 17 - n

num = int(input("Enter the number: "))
res = diff_17(n=num)
print(res)