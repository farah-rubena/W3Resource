'''22. Write a Python program to count the number 4 in a given list.
'''

def count4(numlist):

    count = 0
    for _ in numlist:
        if _ == 4:
            count += 1
    return count

lst = [1,2,4,4,4,5,6,4,5,4]
res = count4(numlist=lst)
print(res)

