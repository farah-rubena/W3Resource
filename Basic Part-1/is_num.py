'''113. Write a Python program that inputs a number and generates an error message if it is not a number.
'''

def check_isnum(num):

    while True:
        if isinstance(num, int):
            return "is number"
        else:
            return "not a number"

    

n = int(input("Enter a number: "))
res = check_isnum(num=n)
print(res)