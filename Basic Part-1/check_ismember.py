''' Write a Python program that checks whether a specified value is contained within a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False

'''

def isamember(num, numlist):

    if num in numlist:
        return True
    return False

n = int(input("Enter a number: "))
lst = [1, 5, 8, 3]
res = isamember(num=n, numlist=lst)
print(res)
