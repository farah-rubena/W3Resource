'''48. Write a Python program to parse a string to float or integer.
'''

def parsestring(text):

    return f"Text as int is {int(float(text))} & as float is {float(text)}"

text = input("Enter numerical text: ")
res = parsestring(text)
print(res)