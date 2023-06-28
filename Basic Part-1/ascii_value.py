'''84. Write a Python program to count the number of occurrences of a specific character in a string.
'''

def asciivalue(char):

    return ord(char)

char = input("Enter the character: ")
res = asciivalue(char)
print(res)