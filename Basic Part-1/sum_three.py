'''18. Write a Python program to calculate the sum of three given numbers. 
If the values are equal, return three times their sum.
'''

def sumthree(a,b,c):

    if a == b == c:
        return (a+b+c) * 3
    return a + b + c

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
res = sumthree(a,b,c)
print(res)