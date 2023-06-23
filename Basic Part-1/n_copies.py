'''20. Write a Python program that returns a string that is n (non-negative integer) copies of a given string.
'''

def ncopies(str, copies):

    return str * copies

str = input("Enter the string: ")
copies = int(input("Enter the copies: "))
res = ncopies(str, copies)
print(res)