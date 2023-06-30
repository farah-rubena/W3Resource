'''112. Write a Python program to remove the first item from a specified list.
'''
def removeitem(lst):

    del lst[0]
    return lst

lst = ["Red", "Black", "Green", "White", "Orange"]
res = removeitem(lst)
print(res)




