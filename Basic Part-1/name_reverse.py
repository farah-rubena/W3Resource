'''Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them.'''

def namereverse(fname, lname):

    return f"{fname[::-1]} {lname[::-1]}"

fname = input("Enter your first name: ")
lname = input("Enter your second name: ")
res = namereverse(fname, lname)
print(res)
