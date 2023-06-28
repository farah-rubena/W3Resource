'''91. Write a Python program to swap two variables.
'''

def swapvar(a,b):

    temp = a
    a = b
    b = temp
    return f"The new valie of a is {a} and the new value of n is {b}"

a = input("Enter the value of a: ")
b = input("Enter the value of a: ")
res = swapvar(a,b)
print(res)