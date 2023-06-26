'''33. Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.
'''

def sum_three(a,b,c):

    if a == b or b == c or c == a:
        return 0
    else:
        return a + b + c 
    
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
res = sum_three(a,b,c)
print(res)


