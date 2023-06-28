'''83. Write a Python program to test whether all numbers in a list are greater than a certain number.
'''

def greaterthan(numlist, num):

    for _ in numlist:
        if _ > num:
            return True
        else:
            return False 

numlist = [5,8,9]
num = int(input("Enter a number to be checked: "))
res = greaterthan(numlist, num)
print(res)