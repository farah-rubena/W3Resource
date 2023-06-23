'''23. Write a Python program to get n (non-negative integer) copies of the
 first 2 characters of a given string. Return n copies of the whole string if the length is less than 2.
'''

def stringcopies(str, copies):

    if len(str) < 2:
        return str * copies
    else:
        return str[:2] * copies

str = input("Enter a string: ")
copies = int(input("Enter the number of copies: "))
res = stringcopies(str, copies)
print(res)

