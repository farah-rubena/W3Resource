'''17. Write a Python program to test whether a number is within 100 of 1000 or 2000.
'''


def within_100(num):

    if ((abs(1000-num) <=100) or (abs(2000-num) <=200)):
        return True
    else:
        return False


n = int(input("Enter the number: "))
res = within_100(num=n)
print(res)