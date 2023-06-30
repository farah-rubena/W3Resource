'''120. Write a Python program to format a specified string and limit the length of a string.
'''


def formatstring(str, strlen):

    new_str = ""
    for _ in range(strlen):
        new_str += str[_]

    return new_str

str = input("Enter a string: ")
strlen = int(input("Enter the lenght limit: "))
res = formatstring(str, strlen)
print(res)