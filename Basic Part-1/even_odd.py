'''21. Write a Python program that determines whether a given number (accepted from the user) is even or odd, 
and prints an appropriate message to the user.
'''

def evenodd(num):

    if num%2 == 0:
        return "Even"
    return "Odd"

n = int(input("Enter a number: "))
res = evenodd(num = n)
print(res)